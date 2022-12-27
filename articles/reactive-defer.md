---
uid: reactive-defer
title: Defer
---

![Marble diagram](~/images/reactive-defer.svg)

The `Defer` operator uses the nested workflow to specify the constructed sequence. All input sequences to the outer `Defer` node will be routed to the inner [WorkflowInput](xref:Bonsai.Expressions.WorkflowInputBuilder) nodes, and all notifications emitted by the inner [WorkflowOutput](xref:Bonsai.Expressions.WorkflowOutputBuilder) node will be emitted by the outer `Defer` node. Multiple subscriptions can be active simultaneously, in which case the nested workflow will run multiple times and is considered to be reentrant.
