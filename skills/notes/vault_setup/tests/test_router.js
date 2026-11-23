// node skills/notes/vault_setup/tests/test_router.js
const Module = require("module");
const path = require("path");
const assert = require("assert");
const orig = Module._resolveFilename;
Module._resolveFilename = function (req, ...a) { return req === "obsidian" ? "obsidian" : orig.call(this, req, ...a); };
require.cache["obsidian"] = { id: "obsidian", filename: "obsidian", loaded: true, exports: {
  Plugin: class {}, SuggestModal: class {}, TFile: class {}, Notice: class {},
  normalizePath: (p) => p.replace(/\\/g, "/").replace(/\/+/g, "/") } };
const P = require(path.join(__dirname, "../assets/plugin_new_note_router/main.js"));
const c = P.__core;
assert.strictEqual(c.cleanTitle("  SQL Injection: Error/Based? "), "sql injection error based");
assert.strictEqual(c.folderFor("concept"), "5_concept");
assert.strictEqual(c.folderFor("nonsense"), "99_other");
assert.strictEqual(c.targetPath("technique", "Second Order SQL"), "2_technique/second order sql.md");
const fm = c.buildFrontmatter({ title: "Error Based SQL", type: "technique", domains: ["web"], references: ["sql injection"], date: new Date(2026, 10, 23), attack: "CWE-89" });
assert.deepStrictEqual(fm, { title: "error based sql", date_created: "2026-11-23", description: "", type: "technique", domain: ["web"], reference: ["[[sql injection]]"], attack: "CWE-89" });
assert.deepStrictEqual(Object.keys(c.buildFrontmatter({ title: "x", type: "concept", date: new Date(2026, 0, 1) })), ["title", "date_created", "description", "type", "domain", "reference"]);
assert.strictEqual(c.skeleton("tool", ""), "- \n\n# References\n");
assert.strictEqual(c.TYPES.length, 8);
// data loss guard: a note with content is never overwritten
const B = String.fromCharCode(92) + "n";
assert.strictEqual(c.newBody("", ""), c.skeleton(null, ""));
assert.strictEqual(c.newBody("   ", "- x"), "- x");
assert.strictEqual(c.newBody("my old note body", ""), null);
assert.strictEqual(c.newBody("---" + B + "title: x" + B + "---", ""), null);
console.log("OK router core");
