---
uid: reactive-condition
title: Condition
---

![Marble diagram](~/images/reactive-condition.svg)

The nested workflow specifying the condition must return a sequence of type <xref href="System.Boolean"/>. This nested sequence may be synchronous or asynchronous with respect to notifications from the source sequence. After each element is emitted by the source sequence, the latest value from the nested sequence is checked. If the value is `true` then the element will be accepted and emitted by the result sequence. Otherwise, the element will be dropped.

### Example

Use `Condition` to filter elements of an observable sequence according to the nested workflow.

:::workflow
![Condition Example](~/workflows/reactive-condition-example.bonsai)
:::

As an example of asynchronous condition evaluation, it is possible to build a simple manual toggle by using a <xref href="Bonsai.Expressions.BooleanProperty"/> connected directly to the output of the nested workflow:

:::workflow
![Condition Asynchronous Example](~/workflows/reactive-condition-asynchronous-example.bonsai)
:::