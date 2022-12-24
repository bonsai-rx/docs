---
uid: expressions-parse
title: "Parse"
---

The `Parse` operator is a [Transform](xref:operators#transform) on sequences of <xref href="System.String"/> values. Each of the strings in the sequence will be matched against the specified <xref href="Bonsai.Expressions.ParseBuilder.Pattern"/> using the .NET regular expression engine (<xref href="System.Text.RegularExpressions.Regex"/>). If a <xref href="Bonsai.Expressions.ParseBuilder.Separator"/> is specified, every input string will first be split using the delimiter, and each substring will then be matched against the regular expression.

The output type is automatically inferred from the structure of the parse pattern. If a separator is used, the output will be an array containing the results of matching each delimited substring against the parse pattern. If any of the values in the input sequence fails to match, an error will be raised and the sequence will be terminated.

> [!Note]
> Multi-character strings can be used to specify both the pattern and the separator. This can sometimes help to parse text formats with more complex tokens. For more flexible or conditional parsing, it is also possible to chain multiple `Parse` operators in a sequence, by matching against the placeholder `%s` at the end of the sequence. This will match and capture any remaining text for downstream processing.

> [!Warning]
> For convenience, both <xref href="Bonsai.Expressions.ParseBuilder.Pattern"/> and <xref href="Bonsai.Expressions.ParseBuilder.Separator"/> properties will accept the use of character escapes to represent specific white space or unicode characters. See the [list of supported character escapes in .NET](https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-escapes-in-regular-expressions#character-escapes-in-net) for more information.

## Examples

The following examples illustrate using different combinations of the <xref href="Bonsai.Expressions.ParseBuilder.Pattern"/> and <xref href="Bonsai.Expressions.ParseBuilder.Separator"/> properties to match different kinds of formatted text data.

| Pattern     | Separator | Type                          | Description | Example |
| ----------- | --------- | ----------------------------- | ----------- | ------- |
| `%f`        |           | [float](xref:System.Single)   | Match a floating-point number. | `5.0` |
| `%f;%i`     |           | [Tuple](xref:System.Tuple`2)<[float](xref:System.Single), [int](xref:System.Int32)>  | Match a floating-point number and an integer separated by a semicolon. | `5.1;5`
| `%f`        | `,`       | [float](xref:System.Single)[] | Match each comma-delimited substring with a floating-point number. | `3.2, 5.6, 8.9` |
| `\(%f,%f\)` | `;`       | [Tuple](xref:System.Tuple`2)<[float](xref:System.Single), [float](xref:System.Single)>[] | Match each semicolon-delimited substring with a pair of floating-point numbers surrounded by parentheses. | `(1, 2); (3.14, 4.5)` |
| `%s,msg:%b` | `\t`      | [Tuple](xref:System.Tuple`2)<[string](xref:System.String), [bool](xref:System.Boolean)>[] | Match each tab-delimited substring with a pattern containing a string and boolean. | `tag1,msg:true tag2,msg:false` |
