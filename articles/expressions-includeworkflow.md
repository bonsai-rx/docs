---
uid: expressions-includeworkflow
title: "IncludeWorkflow"
---

The `IncludeWorkflow` operator works in exactly the same way as [GroupWorkflow](xref:Bonsai.Expressions.GroupWorkflowBuilder), with the difference that the nested workflow definition is stored externally in a file, rather than locally in the node itself. Include nodes are used to organize larger workflows into modular building blocks. They allow reusing functionality across different parts of a workflow, or even across different projects. Changing the definition of an included workflow will be automatically reflected in all places where that workflow is reused.

All observable sequences passed as arguments to the outer `IncludeWorkflow` will be routed to the inner [WorkflowInput](xref:Bonsai.Expressions.WorkflowInputBuilder) nodes. Conversely, all notifications emitted by the sequence connected to the single [WorkflowOutput](xref:Bonsai.Expressions.WorkflowOutputBuilder) node will be passed to any observers of the include workflow node. It is possible to subscribe multiple times to the same include workflow, in which case the nested workflow will run potentially in parallel and is considered to be reentrant.

> [!Note]
> Externalized properties contained inside the included workflow will be exposed when selecting the `IncludeWorkflow` node. Any changes to the values of these properties can be recovered, even if the included workflow is reused multiple times in different parts of the program. They can also be further externalized as part of other nested operators or dynamically assigned using [`PropertyMapping`](xref:Bonsai.Expressions.PropertyMappingBuilder) or [`InputMapping`](xref:Bonsai.Expressions.InputMappingBuilder) operators.

[!include[SharedState](~/articles/expressions-sharedstate.md)]
