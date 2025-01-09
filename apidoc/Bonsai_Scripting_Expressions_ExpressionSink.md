---
uid: Bonsai.Scripting.Expressions.ExpressionSink
---

> [!Warning]
> In general the use of this operator should be avoided. Its main purpose is to trigger or evaluate side-effects in elements of the input sequence, which can break the immutability of values and create confusion. However, in specific applications it might be one of the few ways to interface with a specific API.

[!include[](../articles/scripting-expressions-overview.md)]

### Examples

The following examples demonstrate some actions achievable with this operator.

| Category             | Example                 | Description |
| -------------------- | ----------------------- | ----------- |
| Method Invocation    | `it.Update()`           | Invoke the method `Update` on all the elements of the input sequence. |
| Property Assignment  | `set_Delay(1)`          | Assign a value to the `Delay` property. The expression language does not directly support assignment, but we can refer to the setter method by its canonical identifier `set_P` where `P` is the name of the property. |

> [!Warning]
> Property assignment is only supported on reference types since for value types the expression will be evaluated on a copy of the value. This new value will not be included in the output sequence since a [Sink](../articles/operators.md#sink) operator does not modify the elements of the original sequence.