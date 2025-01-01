---
uid: Bonsai.Scripting.Expressions.ExpressionCondition
---

[!include[](../articles/scripting-expressions-overview.md)]

### Examples

The following examples demonstrate common [Condition](../articles/operators.md#condition) filters achievable with this operator. Elements that evaluate to `true` will pass the filter, while elements that evaluate to `false` will be dropped.

| Category             | Example                     | Description | 
| -------------------- | --------------------------- | ----------- | 
| Comparison Filtering | `it < 3`                    | Filters an element by performing an inline comparison. Inline comparisons can be set using [comparison](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/comparison-operators), [logical](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/boolean-logical-operators), or [equality](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/equality-operators) operators. |
| Predicate Filtering  | `Double.IsPositive(it)`     | Filters an element by calling a type predicate method. For more examples, refer to the C# type documentation - for instance, [Doubles](https://learn.microsoft.com/en-us/dotnet/api/system.double?view=net-7.0#methods). |
| NaN Filtering        | `Double.IsNan(it) == false` | Filters an element by calling the `IsNan` predicate method. This is a special case of predicate filtering, notable because the output must be inverted to exclude `NaN` values. |