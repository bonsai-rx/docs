---
uid: reactive-takewhile
title: TakeWhile
---

![Marble diagram](~/images/reactive-takewhile.svg)

The nested workflow specifying the condition must return a sequence of type <xref href="System.Boolean"/>. This nested sequence may be synchronous or asynchronous with respect to notifications from the source sequence.

After each element is emitted by the source sequence, the latest value from the nested sequence is checked. While the value is `true`, `TakeWhile` will continue to emit all elements from the source sequence. When the value changes to `false`, `TakeWhile` will terminate successfully.

### Examples

Use `TakeWhile` to return elements in an observable sequence as long as the condition specified in the encapsulated workflow is true.

:::workflow
![TakeWhile Example](../workflows/reactive-takewhile-example.bonsai)
:::

### Related Operators

Use [`TakeUntil`](xref:Bonsai.Reactive.TakeUntil) instead to return elements only after a second sequence emits a notification.

Use [`Condition`](xref:Bonsai.Reactive.Condition) instead to filter elements based on the encapsulated workflow.