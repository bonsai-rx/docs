---
uid: reactive-scan
title: Scan
---

![Marble diagram](~/images/reactive-scan.svg)

The nested workflow specifying the accumulation function must return a sequence of the same type as the accumulator. The type of the accumulator is specified by the seed sequence, if an explicit seed sequence is provided as a second input. Otherwise, the accumulator will be of the same type as the elements in the source sequence, and will be initialized to the first element.

When a new element is received from the source sequence, it is paired with the current value in the accumulator and passed as an input notification to the nested workflow. Values emitted by the nested sequence will update the state of the accumulator.

> [!Warning]
> The nested sequence may be synchronous or asynchronous with respect to notifications from the source sequence. However, it is strongly recommended that computation of the accumulation function is performed synchronously to ensure a correspondence between the notifications received from the source sequence and the cumulative values emitted by the result sequence.

### Examples

Use `Scan` to define a custom accumulation function using the encapsulated workflow.

:::workflow
![Scan Example](../workflows/reactive-scan-example.bonsai)
:::

### Related Operators

Use [`Accumulate`](xref:Bonsai.Reactive.Accumulate) instead to compute the running sum of consecutive values.