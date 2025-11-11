---
uid: reactive-tolookup
title: ToLookup
---

![Marble diagram](~/images/reactive-tolookup.svg)

`ToLookup` collects all the values from the source sequence and creates a mapping from keys to a set of elements using the specified <xref href="Bonsai.Reactive.ToLookup.KeySelector"/> and <xref href="Bonsai.Reactive.ToLookup.ElementSelector"/> properties. The [lookup](https://learn.microsoft.com/en-us/dotnet/api/system.linq.lookup-2?view=net-8.0) is emitted when the source sequence completes successfully, and will have key and element types matching the selected members.

> [!Note]
> A lookup allows multiple values to be grouped under the same key.

[!include[ToCollection](~/articles/reactive-tocollection.md)]

### Examples

Use `ToLookup` to create a lookup from an observable sequence according to the specified key and element selector.

:::workflow
![ToLookup Example](../workflows/reactive-tolookup-example.bonsai)
:::

### Related Operators

Use [`ToDictionary`](xref:Bonsai.Reactive.ToDictionary) to link single elements to keys.