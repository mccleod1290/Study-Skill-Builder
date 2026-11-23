---
title: error based sql
date_created: {{date}}
description: Break the query on purpose. The error shows data.
type: technique
domain:
  - web
reference:
  - "[[sql injection]]"
attack: CWE-89
---
- Needs: the database error reaches the client.
- Cast or convert a value into the wrong type. The error prints it.

# Detecting

- A single quote returns a database error.

# Defense

- Generic error page. [[parameterized query]].

# References
