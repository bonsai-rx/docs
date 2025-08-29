---
uid: reactive-ignoreelements
title: IgnoreElements
---

![Marble diagram](~/images/reactive-ignoreelements.svg)

> [!Tip]
> This operator can sometimes be useful when only the type of the sequence is important, and not its elements. The compiler will still check the correct type of the sequence even if no elements are emitted.

### Examples

Use `IgnoreElements` to ignore all elements, leaving only termination messages.

:::workflow
![IgnoreElements Example](../workflows/reactive-ignoreelements-example.bonsai)
:::