---
uid: expressions-workflowoutput
title: "WorkflowOutput"
---

The `WorkflowOutput` operator is used inside nested workflows to specify the sequence of notifications providing the result of the nested function. In each workflow there can only be at most one `WorkflowOutput` node. How this result sequence is converted into the sequence of notifications of the outer nesting node is dependent on the exact operator in which the output is nested.

If no `WorkflowOutput` is specified, the result sequence of any nested workflow (including the top-level workflow) will be of type [Unit](xref:System.Reactive.Unit) and will not emit any notifications except for successful termination if all inner sequences terminate successfully, or exceptional termination if any of the inner sequences raises an error.

> [!Note]
> If the sequence connected to `WorkflowOutput` terminates successfully, all other nested operators will be immediately cancelled. This is also true for the top-level workflow, in which case the entire program execution is terminated.
