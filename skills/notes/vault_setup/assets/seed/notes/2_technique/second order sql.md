---
title: second order sql
date_created: {{date}}
description: Stored safely, used unsafely on another page.
type: technique
domain:
  - web
reference:
  - "[[sql injection]]"
attack: CWE-89
---
- Input passes the first check. A later query reuses it.
- Scanners miss it. The payload and the trigger are different requests.

# Detecting

- Follow each stored value to every page that reads it.

# References
