---
title: union based sql
date_created: {{date}}
description: UNION adds a second SELECT. Its rows appear in the page.
type: technique
domain:
  - web
reference:
  - "[[sql injection]]"
attack: CWE-89
---
- Needs: same column count, compatible types.
- Find the count first. Then find a column that prints text.

# Detecting

- ORDER BY n, raise n until the page errors.

# References
