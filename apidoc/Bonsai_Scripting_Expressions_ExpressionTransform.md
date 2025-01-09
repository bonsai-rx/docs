---
uid: Bonsai.Scripting.Expressions.ExpressionTransform
---

[!include[](../articles/scripting-expressions-overview.md)]

## Examples

The following examples demonstrate common [Transforms](../articles/operators.md#transform) achievable with this operator.

| Category               | <div style="width:210px">Example</div> | Description | 
| ---------------------- | ----------------------------- | -------------------- | 
| Arithmetic Operations  | `1.0 / (it + 2.0)`            | Transform an element using [arithmetic operators](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators). |
| Arithmetic Operations  | `Math.Sqrt(it)`               | Transform an element using functions provided by the [Math](https://learn.microsoft.com/en-us/dotnet/api/system.math) class. |
| Attribute Renaming     | `new(Item1 as X, Item2 as Y)` | Project the members of an element into a new data object. Commonly used to rename object attributes. | 
| Conditional Expression | `it ? 1 : 0 `                 | Convert a `Boolean` value into an integer or numerical type. |
| Type Conversion        | `Double(it)`                  | Explicitly convert a primitive numeric type to a `Double`. |
| Type Conversion        | `Convert.ToDouble(it)`        | Convert an element of any primitive type (including `String` values) to a `Double` using the [Convert](https://learn.microsoft.com/en-us/dotnet/api/system.convert) class. |
| Type Conversion        | `TimeSpan.FromSeconds(it)`    | Convert a primitive value type into another type by directly invoking a static method in the target type. |