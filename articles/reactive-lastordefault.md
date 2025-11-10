---
uid: reactive-lastordefault
title: LastOrDefault
---

![Marble diagram](~/images/reactive-lastordefault.svg)

If the sequence has no elements, `LastOrDefault` will emit a [default](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/default-values) value before terminating successfully. 

> [!Tip]
> `LastOrDefault` is one of the simplest and most efficient ways of capturing the end of an observable sequence explicitly as a notification in the workflow. You can use it to react to the termination of a sequence regardless of whether that sequence produces values.

### Examples

Use `LastOrDefault` to retrieve the last element of a sequence or a default value if the sequence is empty.

:::workflow
![LastOrDefault Example](../workflows/reactive-lastordefault-example.bonsai)
:::

### Related Operators

Use [`TakeLast`](xref:Bonsai.Reactive.TakeLast) to retrieve one or more elements from the end of the sequence.

This is a subtle but important difference between the `LastOrDefault` operator and [`TakeLast(1)`](xref:Bonsai.Reactive.TakeLast), which will also complete successfully when the source sequence is empty, but will not emit any values.