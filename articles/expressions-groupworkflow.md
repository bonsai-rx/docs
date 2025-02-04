---
uid: expressions-groupworkflow
title: "GroupWorkflow"
---

The workflow nested inside `GroupWorkflow` specifies the entire behavior of this operator. Group nodes are used to organize larger workflows into modular building blocks. For most purposes, moving operations into a group workflow will not have any effects on the performance or function of the program.

All observable sequences passed as arguments to the outer `GroupWorkflow` will be routed to the inner [WorkflowInput](xref:Bonsai.Expressions.WorkflowInputBuilder) nodes. Conversely, all notifications emitted by the sequence connected to the single [WorkflowOutput](xref:Bonsai.Expressions.WorkflowOutputBuilder) node will be passed to any observers of the group node. It is possible to subscribe multiple times to the same group, in which case the nested workflow will run potentially in parallel and is considered to be reentrant.

> [!Tip]
> Use [`ExternalizedMapping`](xref:Bonsai.Expressions.ExternalizedMappingBuilder) operators to expose configurable properties when selecting the nested workflow node. Externalized properties in a nested workflow work the same way as regular properties in other operators. They can be further externalized as part of other nested operators or dynamically assigned using [`PropertyMapping`](xref:Bonsai.Expressions.PropertyMappingBuilder) or [`InputMapping`](xref:Bonsai.Expressions.InputMappingBuilder) operators.

[!include[SharedState](~/articles/expressions-sharedstate.md)]
