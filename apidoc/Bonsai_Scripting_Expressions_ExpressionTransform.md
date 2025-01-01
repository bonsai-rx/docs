---
uid: Bonsai.Scripting.Expressions.ExpressionTransform
---

[!include[](../articles/scripting-expressions-overview.md)]

### Examples

The following examples demonstrate common [Transforms](../articles/operators.md#transform) achievable with this operator.

| Category               | Example                             | Description | 
| ---------------------- | -------------------------------     | ----------- | 
| Arithmetic Operations  | `1.0 / (it + 2.0)`                  | Transforms an element using [arithmetic operators](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators). |
| Arithmetic Operations  | `Math.Sqrt(it)`                     | Transforms an element using functions provided by the [Math](https://learn.microsoft.com/en-us/dotnet/api/system.math?view=net-7.0) class. |
| Attribute Renaming     | `new(it.Item1 as X, it.Item2 as Y)` | Transforms an element's field name. Commonly used to rename column headers for the [`CsvWriter`](xref:Bonsai.IO.CsvWriter) node. | 
| Conditional Expression | `it ? 1 : 0 `                       | Transforms an element by returning the first value if `it` is `true`, and the second value otherwise, using the conditional operator [`?`](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/conditional-operator). It can be placed directly after an node that outputs a Boolean value such as [`Equal`](xref:Bonsai.Expressions.EqualBuilder). It can also be used for type conversion. |
| Conditional Expression | `it < 3 ? 1 : 0 `                   | Transforms an element by returning the first or second value after performing an inline comparison. Inline comparisons can be set using [comparison](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/comparison-operators), [logical](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/boolean-logical-operators), or [equality](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/equality-operators) operators. |
| Type Conversion        | `Convert.ToDouble(it)`              | Transforms an element's type using the [Convert](https://learn.microsoft.com/en-us/dotnet/api/system.convert?view=net-7.0) class. |
| Type Conversion        | `TimeSpan.FromSeconds(it)`          | Transforms an element's type by directly invoking an output type's method. Simplifies the required input formatting in some cases. |

> [!Note]
> The expressions can be combined for additional flexibility.