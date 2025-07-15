---
uid: reactive-distinctuntilchanged
title: DistinctUntilChanged
---

![Marble diagram](~/images/reactive-distinctuntilchanged.svg)

The `DistinctUntilChanged` operator removes all contiguous elements in the sequence that are equal. Equality is determined by the default <xref href="System.Collections.Generic.EqualityComparer`1"/> for the type of the elements in the source sequence.

In other words, after each element is emitted by the result sequence, subsequent elements will be dropped until the value changes.

### Example

Use `DistinctUntilChanged` to filter only elements which are distinct from the previous element.

:::workflow
![DistinctUntilChanged Example](../workflows/reactive-distinctuntilchanged-example.bonsai)
:::

#### Signal State Transitions

Use `DistinctUntilChanged` to signal changes in state, such as when an object enters or leaves a region of interest.

:::workflow
![DistinctUntilChanged Application StateTransitions](../workflows/reactive-distinctuntilchanged-application-statetransitions.bonsai)
:::

> [!NOTE]
> This example requires the `Bonsai.WindowsInput` package to be installed.
