---
uid: expressions-unit
title: "Unit"
---

The `Unit` operator generates a sequence returning the singleton unit object, if no input sequence is provided. Otherwise, it will convert all elements in the source sequence to the <xref href="System.Reactive.Unit"/> type.

> [!Tip]
> `Unit` is most commonly used for converting separate branches with different types into a common type signature, so they can be combined using control flow operators such as [`Merge`](xref:Bonsai.Reactive.Merge) or [`Concat`](xref:Bonsai.Reactive.Concat).
