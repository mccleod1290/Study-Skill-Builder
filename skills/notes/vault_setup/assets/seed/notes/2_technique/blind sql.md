---
title: blind sql
date_created: {{date}}
description: No data comes back. Ask yes or no questions.
type: technique
domain:
  - web
reference:
  - "[[sql injection]]"
attack: CWE-89
---
- Boolean: the page differs for true and false.
- Time: the response delay is the answer.
- Slow. Script it.

# Detecting

- Add a true condition and a false one. Compare the responses.

# References
