---
uid: reactive-tolist
title: ToList
---

![Marble diagram](~/images/reactive-tolist.svg)

`ToList` emits a single [list](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/collections) of the same type as the type of the elements in the source sequence. The list is emitted when the source sequence completes successfully.

[!include[ToCollection](~/articles/reactive-tocollection.md)]

### Examples

Use `ToList` to create a list with every element in the sequence.

:::workflow
![ToList Example](../workflows/reactive-tolist-example.bonsai)
:::

### Related Operators

Use [`ToArray`](xref:Bonsai.Reactive.ToArray) if you do not need to manipulate elements in the collection.