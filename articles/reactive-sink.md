---
uid: reactive-sink
title: Sink
---

![Marble diagram](~/images/reactive-sink.svg)

The `Sink` operator uses the nested workflow to specify a reactive operation over the elements of the source sequence. `Sink` emits all values from the source sequence directly without modification, and the nested sequence is subscribed to purely for its side-effects. All notifications emitted by the inner [WorkflowOutput](xref:Bonsai.Expressions.WorkflowOutputBuilder) node are ignored.

> [!Tip]
> `Sink` operators are very useful to prevent side-effects from affecting the source sequence. Even if the inner sequence terminates early, or changes the timing of emitted values, these effects will not propagate to the outer sequence.

> [!Warning]
> If the source sequence terminates, the subscription to the nested sequence will be cancelled. If the reactive operation needs to be fully asynchronous and decoupled from the main sequence, consider using @subjects to process items in a separate branch of the workflow.
