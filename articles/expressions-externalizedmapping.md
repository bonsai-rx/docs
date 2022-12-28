---
uid: expressions-externalizedmapping
title: "ExternalizedMapping"
---

> [!Warning]
> In any one workflow, it is not possible to have more than one externalized property with the same name. When externalizing multiple conflicting properties, you can use the [`DisplayName`](xref:Bonsai.Expressions.ExternalizedMapping.DisplayName) property of the externalized mapping to provide distinct unique names for each property. It is also possible to specify different category or description strings to the externalized property for documentation purposes.

When externalized properties are nested inside an operator group, for example inside a [`GroupWorkflow`](xref:Bonsai.Expressions.GroupWorkflowBuilder), they will be exposed as member properties of the node group itself. This means that when the group node is selected, all named externalized properties will show up in the `Properties` panel.