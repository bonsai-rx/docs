---
uid: reactive-visualizer
title: Visualizer
---

![Marble diagram](~/images/reactive-visualizer.svg)

The `Visualizer` operator is a [Sink](xref:Bonsai.Reactive.Sink) which uses the nested workflow to specify a reactive visualizer function over the elements of the source sequence. `Visualizer` emits all values from the source sequence directly without modification, and the nested sequence is subscribed to purely for its side-effects.

> [!Note]
> All notifications emitted by the inner [`WorkflowOutput`](xref:Bonsai.Expressions.WorkflowOutputBuilder) node are ignored. However, the type visualizer assigned to the nested workflow output will be considered as the default visualizer of the outer node.

### Examples

Use `Visualizer` to use the encapsulated workflow as a visualizer.

:::workflow
![Visualizer Example](../workflows/reactive-visualizer-example.bonsai)
:::