---
uid: expressions-propertymapping
title: "PropertyMapping"
---

The connection between the property mapping and its target node only affects the state of properties. The behaviour of the operator will otherwise remain unaffected, since the subscription to the mapping is not considered as a proper upstream source. This is indicated in the editor by the dashed line linking the property mapping operator to its target.

> [!Warning]
> Because property values are updated independently, this means that values can change even while the target operator is reacting to notifications from other nodes. Care must be taken to ensure that changing the property state in this way does not break the behaviour of the workflow.
>
> Specifically, some operators respond to changes in their parameters only at specific moments. For example, the parameters of the [`Timer`](xref:Bonsai.Reactive.Timer) operator must be set before the observable sequence is initialized. In this case, the input to the externalized property needs to be emitted immediately during the subscription phase for the mapping to work.