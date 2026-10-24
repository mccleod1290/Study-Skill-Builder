# Email setup (Gmail app password)

The email step uses `skills/scripts/send_notes_email.py`. It reads SMTP settings from a file **outside the repo**. The password never goes in the code, in git, or in chat.

## One time

1. Turn on 2-Step Verification on your Google account.
2. Make an app password: Google account -> Security -> App passwords. Google shows a 16-character code once.
3. Create `~/.config/study-os/smtp.env` (on Windows: `%USERPROFILE%\.config\study-os\smtp.env`) with:

   ```
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=<your-email>
   SMTP_APP_PASSWORD=the 16 character app password
   SMTP_TO=<your-email>
   ```

4. Lock it down: `chmod 600 ~/.config/study-os/smtp.env`.

## Rules

- The app password lives only in that file. It is not a file in this repo. Do not paste it into chat, a skill, or the email body.
- An app password is not your Google password. Revoke it any time from the same App passwords page.
- `send_notes_email.py` reads the file and sends. It sends only when you ask.

## Test

```
python skills/scripts/send_notes_email.py --subject "test" --body "hello" some_file.html
```
