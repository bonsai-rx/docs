---
uid: expressions-parse
title: "Parse"
---

The `Parse` operator is a [Transform](xref:operators#transform) on sequences of <xref href="System.String"/> values. Each of the strings in the sequence will be matched against the specified <xref href="Bonsai.Expressions.ParseBuilder.Pattern"/> using the .NET regular expression engine (<xref href="System.Text.RegularExpressions.Regex"/>). If a <xref href="Bonsai.Expressions.ParseBuilder.Separator"/> is specified, every input string will first be split into substrings using the specified delimiter before passing them into the regular expression.

The output type is automatically inferred from the structure of the parse pattern. If a separator is used, the output will be an array storing the results of matching each delimited substring against the parse pattern. If any of the values in the input sequence fails to match against the specified pattern, an error will be raised and the sequence will be terminated. For more flexible parsing, it is possible to chain multiple `Parse` operators in a sequence by parsing only specific sub-strings of the input, and passing the remainder of the string downstream for further processing.

## Examples

The following examples illustrate using different combinations of the <xref href="Bonsai.Expressions.ParseBuilder.Pattern"/> and <xref href="Bonsai.Expressions.ParseBuilder.Separator"/> properties to match different kinds of formatted text data.

| Pattern    | Separator | Type                          | Description |
| ---------- | --------- | ----------------------------- | ----------- |
| `%f`       |           | [float](xref:System.Single)   | Match a floating-point number. |
| `%f;%i`    |           | [Tuple](xref:System.Tuple`2)<[float](xref:System.Single), [int](xref:System.Int32)>  | Match a floating-point number and an integer separated by a semi-colon. |
| `%f`       | `,`       | [float](xref:System.Single)[] | Match each comma-delimited substring with a floating-point number. |
| `%s,%b`    | `\t`      | [Tuple](xref:System.Tuple`2)<[string](xref:System.String), [bool](xref:System.Boolean)>[] | Match each tab-delimited substring with a pair of string and boolean, separated by a comma. |
