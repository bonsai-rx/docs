---
uid: reactive-max
title: Max
---

![Marble diagram](~/images/reactive-max.svg)

The `Max` operator collects all the values from the source sequence and emits a single value representing the largest of all values. The single result value is emitted only when the source sequence terminates successfully.

### Example
Use `Max` to report the minimum value (such as the interval between key presses) at the end of the sequence.

:::workflow
![Minimum](../workflows/reactive-max-example.bonsai)
:::

> [!NOTE]
> The [`Delay`](xref:Bonsai.Reactive.Delay) operator is used in this example only to keep the workflow open long enough to visualize the result. Since only a single value is emitted, use an [`ObjectTextVisualizer`](xref:Bonsai.Design.ObjectTextVisualizer) to visualize it.