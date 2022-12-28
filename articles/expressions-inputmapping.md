---
uid: expressions-inputmapping
title: "InputMapping"
---

Fundamentally, the `InputMapping` operator works exactly the same way as [`PropertyMapping`](xref:Bonsai.Expressions.PropertyMappingBuilder), but now the connection from the mapping operator to its target node is done through the upstream sources. In this case, only values from the source sequence can be used to map properties in the target node. However, it is possible to specify which specific member of the original data source will be selected as input to the target node by setting the [Selector](xref:Bonsai.Expressions.InputMappingBuilder.Selector) property.

Whenever the original input sequence sends out a new data item, all the specified property mappings will be updated at the same time before this item is finally allowed to go through and notify the target. In this way, you can be sure that no property changes are performed between upstream notifications.