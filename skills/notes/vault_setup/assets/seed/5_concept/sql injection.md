---
title: sql injection
date_created: {{date}}
description: User input changes the query, not just its data.
type: concept
domain:
  - web
reference: []
---
- Input is read as query code.
- [[error based sql]]: the error text leaks data.
- [[union based sql]]: appended rows come back in the page.
- [[blind sql]]: no data back. Read true or false, or a delay.
- [[second order sql]]: stored now, run later.
- Fix: [[parameterized query]]. Data never becomes code.

# References

- [PortSwigger: SQL injection](https://portswigger.net/web-security/sql-injection)
