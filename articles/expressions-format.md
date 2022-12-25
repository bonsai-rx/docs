---
uid: expressions-format
title: "Format"
---

The `Format` operator is a [Transform](xref:operators#transform) that can be applied on sequences of any type. Each of the elements in the sequence will be converted to a <xref href="System.String"/> value using the specified <xref href="Bonsai.Expressions.FormatBuilder.Format"/>. The format string follows the same syntax of the [String.Format](xref:System.String.Format*) method. The <xref href="Bonsai.Expressions.FormatBuilder.Selector"/> property can be used to specify the order of the values that will be converted to strings and inserted at a specified place in the format string.

If no format string is specified, the default [ToString](xref:System.Object.ToString) method is used to convert each value in the sequence.

### Example

You can use the `Format` operator to insert the value of a sequence into another string. For example, the following workflow and format string visualizes the value and timestamp of each tick of a timer:

:::workflow
![Example workflow](~/workflows/expressions-format-example.bonsai)
:::

```
Received value {0} at time {1}.
```

Both `{0}` and `{1}` are format items. The index `0` refers to the first member specified in the <xref href="Bonsai.Expressions.FormatBuilder.Selector"/> property of the `Format` node (in this case `Value`). Index `1` refers to the second member (in this case `Timestamp`). The output will be similar to:

```
Received value 9 at time 12/25/2022 22:15:06 +00:00.
```

We can specify a format string for the second member to remove the date part of the timestamp:

```
Received value {0} at time {1:T}.
```

Which will then produce the following output:

```
Received value 9 at time 22:15:06.
```

For more formatting examples and a comprehensive list of supported format strings for different data types, see the extended discussion section for the [String.Format](xref:System.String.Format*) method.
