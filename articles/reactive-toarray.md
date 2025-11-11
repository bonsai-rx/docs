---
uid: reactive-toarray
title: ToArray
---

![Marble diagram](~/images/reactive-toarray.svg)

`ToArray` emits a single [array](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/arrays) of the same type as the type of the elements in the source sequence. The array is emitted when the source sequence completes successfully.

[!include[ToCollection](~/articles/reactive-tocollection.md)]

### Examples

Use `ToArray` to create an array with every element in an observable sequence.

:::workflow
![ToArray Example](../workflows/reactive-toarray-example.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.Design.Visualizers` package to be installed.

#### Collect Input Data

Use `ToArray` to collect a sequence of individual elements produced by file reading operators such as [`CsvReader`](xref:Bonsai.IO.CsvReader).

:::workflow
![ToArray Application](../workflows/reactive-toarray-application-collectinputdata.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.IO` package to be installed.

### Related Operators

Use [`ToList`](xref:Bonsai.Reactive.ToList) if you need to add or remove elements from the collection.