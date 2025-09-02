---
uid: reactive-skipwhile
title: SkipWhile
---

![Marble diagram](~/images/reactive-skipwhile.svg)

The nested workflow specifying the condition must return a sequence of type <xref href="System.Boolean"/>. This nested sequence may be synchronous or asynchronous with respect to notifications from the source sequence.

After each element is emitted by the source sequence, the latest value from the nested sequence is checked. While the value is `true`, elements will continue to be dropped from the result sequence. When the value changes to `false`, `SkipWhile` will start emitting all elements from the source sequence.

If the source sequence terminates before the nested workflow returns `false`, `SkipWhile` will terminate without emitting any values.

### Example

Use `SkipWhile` to bypass elements in an observable sequence as long as the condition specified in the encapsulated workflow is true.

:::workflow
![SkipWhile Example](../workflows/reactive-skipwhile-example.bonsai)
:::

### Alternatives

Use [`SkipUntil`](xref:Bonsai.Reactive.SkipUntil) instead to return elements only after a second sequence emits a notification.

Use [`Condition`](xref:Bonsai.Reactive.Condition) instead to filter elements based on the encapsulated workflow.