---
uid: reactive-tolookup
title: ToLookup
---

![Marble diagram](~/images/reactive-tolookup.svg)

`ToLookup` collects all the values from the source sequence and creates a mapping from keys to a set of elements using the specified <xref href="Bonsai.Reactive.ToLookup.KeySelector"/> and <xref href="Bonsai.Reactive.ToLookup.ElementSelector"/> properties. The lookup is emitted when the source sequence completes successfully, and will have key and element types matching the selected members.

> [!Note]
> A lookup allows multiple values to be grouped under the same key.

[!include[ToCollection](~/articles/reactive-tocollection.md)]
