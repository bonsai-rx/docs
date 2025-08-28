---
uid: reactive-minby
title: MinBy
---

![Marble diagram](~/images/reactive-minby.svg)

The `MinBy` operator collects all the specified keys from values in the source sequence and emits a single value representing the value with the smallest key. The single result value is emitted only when the source sequence terminates successfully.

### Example

Use `MinBy` to return the list of values with the smallest key.

:::workflow
![MinBy Example](../workflows/reactive-minby-example.bonsai)
:::