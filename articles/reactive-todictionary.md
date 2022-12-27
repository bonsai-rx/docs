---
uid: reactive-todictionary
title: ToDictionary
---

![Marble diagram](~/images/reactive-todictionary.svg)

`ToDictionary` collects all the values from the source sequence and creates a dictionary mapping keys to elements using the specified <xref href="Bonsai.Reactive.ToDictionary.KeySelector"/> and <xref href="Bonsai.Reactive.ToDictionary.ElementSelector"/> properties. The dictionary is emitted when the source sequence completes successfully, and will have key and element types matching the selected members.

> [!Warning]
> If the source sequence emits a value with a duplicate key, an error will be raised and the sequence will terminate exceptionally.

[!include[ToCollection](~/articles/reactive-tocollection.md)]
