/* new-note-router. local plugin, no network, no dependencies.
   flow (after Helton's obsidian v2 video): new note -> type -> name -> domain (multi) -> references (multi, optional)
   -> frontmatter written, body skeleton applied, note moved to its type folder.
   cancel at any step: the note stays in the inbox, untouched. */
const obsidian = require("obsidian");
const { Plugin, SuggestModal, TFile, Notice, normalizePath } = obsidian;

const TYPES = [
  { id: "technology", folder: "1_technology" },
  { id: "technique", folder: "2_technique" },
  { id: "research", folder: "3_research" },
  { id: "tool", folder: "4_tool" },
  { id: "concept", folder: "5_concept" },
  { id: "prompt", folder: "6_prompt" },
  { id: "bookmark", folder: "7_bookmark" },
  { id: "other", folder: "99_other" },
];
const DOMAINS = ["web", "cloud", "ai", "linux", "windows", "macos", "mobile", "kubernetes", "network", "redteam", "blueteam", "career", "other"];
const DONE = "Done selecting";
const META = "_obsidian";
const INBOX = META + "/inbox";
const TEMPLATES = META + "/templates";

/* ---------- pure core (tested in node, see tests/test_router.js) ---------- */
function cleanTitle(raw) {
  return String(raw || "").replace(/[\\/:*?"<>|#^\[\]]/g, " ").replace(/\s+/g, " ").trim().toLowerCase();
}
function folderFor(type) {
  const t = TYPES.find((x) => x.id === type) || TYPES[TYPES.length - 1];
  return t.folder;
}
function targetPath(type, title) {
  return normalizePath(folderFor(type) + "/" + cleanTitle(title) + ".md");
}
function isoDate(d) {
  const p = (n) => String(n).padStart(2, "0");
  return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate());
}
function buildFrontmatter(o) {
  const fm = {
    title: cleanTitle(o.title),
    date_created: isoDate(o.date || new Date()),
    description: "",
    type: o.type,
    domain: o.domains || [],
    reference: (o.references || []).map((r) => "[[" + r + "]]"),
  };
  if (o.type === "technique") fm.attack = o.attack || "";
  return fm;
}
function skeleton(type, templateText) {
  if (templateText && templateText.trim()) return templateText.replace(/\r\n/g, "\n");
  return "- \n\n# References\n";
}
/* ---------- /pure core ---------- */

class ChoiceModal extends SuggestModal {
  constructor(app, placeholder, choices, onChoose, onCancel) {
    super(app);
    this.choices = choices;
    this.onChoose = onChoose;
    this.onCancel = onCancel;
    this.chosen = false;
    this.setPlaceholder(placeholder);
  }
  getSuggestions(q) {
    const s = q.toLowerCase();
    return this.choices.filter((c) => c.toLowerCase().includes(s));
  }
  renderSuggestion(v, el) { el.setText(v); }
  onChooseSuggestion(v) { this.chosen = true; this.onChoose(v); }
  onClose() {
    // the modal closes before the choose callback runs, so defer the cancel check
    setTimeout(() => { if (!this.chosen) this.onCancel(); }, 0);
  }
}
function ask(app, placeholder, choices) {
  return new Promise((resolve) => new ChoiceModal(app, placeholder, choices, resolve, () => resolve(null)).open());
}
async function askMany(app, label, choices, optional) {
  const picked = [];
  for (;;) {
    const left = choices.filter((c) => !picked.includes(c));
    const v = await ask(app, label + " (" + picked.length + " selected)" + (optional ? " (optional)" : ""), [DONE].concat(left));
    if (v === null) return null;
    if (v === DONE) return picked;
    picked.push(v);
  }
}
class TextModal extends SuggestModal {
  constructor(app, placeholder, initial, resolve) {
    super(app);
    this.setPlaceholder(placeholder);
    this.initial = initial;
    this.resolveFn = resolve;
    this.done = false;
  }
  onOpen() {
    super.onOpen();
    if (this.initial) { this.inputEl.value = this.initial; this.inputEl.dispatchEvent(new Event("input")); }
  }
  getSuggestions(q) { return q.trim() ? [q.trim()] : []; }
  renderSuggestion(v, el) { el.setText("name: " + cleanTitle(v)); }
  onChooseSuggestion(v) { this.done = true; this.resolveFn(v); }
  onClose() { setTimeout(() => { if (!this.done) this.resolveFn(null); }, 0); }
}
function askName(app, placeholder, initial) {
  return new Promise((resolve) => new TextModal(app, placeholder, initial, resolve).open());
}

module.exports = class NewNoteRouter extends Plugin {
  async onload() {
    this.busy = new Set();
    this.app.workspace.onLayoutReady(() => {
      this.registerEvent(this.app.vault.on("create", (f) => this.onCreate(f)));
    });
    this.addCommand({
      id: "route-active-note",
      name: "Route this note (type, domain, references)",
      callback: () => { const f = this.app.workspace.getActiveFile(); if (f) this.route(f); },
    });
  }
  async onCreate(file) {
    if (!(file instanceof TFile) || file.extension !== "md") return;
    if (file.path.startsWith(META + "/") && !file.path.startsWith(INBOX + "/")) return;
    if (this.busy.has(file.path)) return;
    // only brand-new empty notes. sync, imports and clippings are not interrupted
    await new Promise((r) => setTimeout(r, 150));
    const text = await this.app.vault.read(file).catch(() => null);
    if (text === null || text.trim() !== "") return;
    this.route(file);
  }
  async route(file) {
    const app = this.app;
    this.busy.add(file.path);
    try {
      const type = await ask(app, "Select the note type", TYPES.map((t) => t.id));
      if (type === null) return;
      const initial = /^untitled/i.test(file.basename) ? "" : file.basename;
      const name = await askName(app, "Note name", initial);
      if (name === null) return;
      const domains = await askMany(app, "Select domain", DOMAINS, false);
      if (domains === null) return;
      let attack = "";
      if (type === "technique") {
        // free text: ATT&CK id, CWE or OWASP id. empty is fine
        const a = await askName(app, "ATT&CK, CWE or OWASP id (optional)", "");
        attack = a === null ? "" : a;
      }
      const notes = app.vault.getMarkdownFiles()
        .filter((f) => !f.path.startsWith(META + "/") && f.path !== file.path)
        .map((f) => f.basename).sort();
      const refs = await askMany(app, "Select a note to reference", notes, true);
      if (refs === null) return;

      const dest = targetPath(type, name);
      if (app.vault.getAbstractFileByPath(dest) && dest !== file.path) {
        new Notice("A note named '" + cleanTitle(name) + "' already exists in " + folderFor(type) + ". Nothing changed.");
        return;
      }
      const tplFile = app.vault.getAbstractFileByPath(TEMPLATES + "/" + type + ".md");
      const tpl = tplFile instanceof TFile ? await app.vault.read(tplFile) : "";
      await app.vault.modify(file, skeleton(type, tpl));
      await app.fileManager.processFrontMatter(file, (fm) =>
        Object.assign(fm, buildFrontmatter({ title: name, type, domains, references: refs, attack })));
      this.busy.add(dest);
      await app.fileManager.renameFile(file, dest);
      await app.workspace.getLeaf(false).openFile(app.vault.getAbstractFileByPath(dest));
    } catch (e) {
      new Notice("new-note-router: " + (e && e.message ? e.message : e));
    } finally {
      this.busy.delete(file.path);
    }
  }
};
module.exports.__core = { cleanTitle, folderFor, targetPath, buildFrontmatter, skeleton, TYPES, DOMAINS };
