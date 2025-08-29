---
uid: reactive-selectmany
title: SelectMany
---

![Marble diagram](~/images/reactive-selectmany.svg)

For each notification in the source sequence, `SelectMany` constructs and subscribes to the results of an asynchronous operation specified in the nested workflow. If multiple asynchronous operations are launched simultaneously, `SelectMany` will merge all the results into a single sequence.

The input to the nested workflow represents the element passed as an argument to the asynchronous operation. If the input is itself an observable sequence, the [WorkflowInput](xref:Bonsai.Expressions.WorkflowInputBuilder) node will subscribe to all the values in the sequence when the asynchronous operation is launched. Otherwise, the input will emit a single value containing the stored argument value.

> [!Tip]
> `SelectMany` is one of the most versatile reactive operators and can be used as a primitive building block on which to build a large number of more complex reactive operators, including reactive state machines. See the [State Machines tutorial](xref:state-machines-tutorial) for examples.

### Example

Use `SelectMany` to create higher-order observable sequences and merge them into a single sequence.

:::workflow
![SelectMany Example](../workflows/reactive-selectmany-example.bonsai)
:::

### Alternatives

Use [`CreateObservable`](xref:Bonsai.Reactive.CreateObservable) instead to create separate higher-order observable sequences.