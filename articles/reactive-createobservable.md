---
uid: reactive-createobservable
title: CreateObservable
---

![Marble diagram](~/images/reactive-createobservable.svg)

For each notification in the source sequence, `CreateObservable` constructs a new instance of the asynchronous operation specified in the nested workflow and emits the operation exposed as an observable sequence. However, `CreateObservable` does not itself subscribe to the sequence, which means the logic inside the nested workflow will not run unless the emitted observables are subscribed downstream.

> [!Note]
> You can manipulate and schedule each of the emitted observable sequences downstream using higher-order operators such as [`Merge`](xref:Bonsai.Reactive.Merge), [`Concat`](xref:Bonsai.Reactive.Concat) or [`Switch`](xref:Bonsai.Reactive.Switch).

The input to the nested workflow represents the element passed as an argument to the asynchronous operation. If the input is itself an observable sequence, the [WorkflowInput](xref:Bonsai.Expressions.WorkflowInputBuilder) node will subscribe to all the values in the sequence when the asynchronous operation is finally launched. Otherwise, the input will emit a single value containing the stored argument value.

### Example

Use `CreateObservable` to create higher-order observable sequences.

:::workflow
![CreateObservable Example](../workflows/reactive-createobservable-example.bonsai)
:::

### Related Operators

Use [`SelectMany`](xref:Bonsai.Reactive.SelectMany) instead to create higher-order observable sequences and merge them into a single sequence.