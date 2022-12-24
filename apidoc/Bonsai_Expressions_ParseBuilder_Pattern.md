---
uid: Bonsai.Expressions.ParseBuilder.Pattern
remarks: *content
---

The parse pattern may contain zero or more placeholder characters. Each placeholder is always preceded by the character `%`, and must specify one of the allowed data type format specifiers (see table below). For each placeholder in the pattern, the `Parse` method of the corresponding data type will be called to convert the matched string to an equivalent instance of that type.

> [!Note]
> Some placeholder conversions will account for white space characters surrounding the input, e.g. the parse pattern `%i,%i` will work the same for `1,2` or `1, 2`.

> [!Warning]
> All parse conversions are done using the [invariant culture](xref:System.Globalization.CultureInfo.InvariantCulture). Specifying culture-specific conversions is not currently supported. There is also no support for implicit numeric conversions, e.g. attempting to parse `5.0` using `%i` will throw an error.

If the parse pattern is `null` or empty, the operator will simply return the raw input value. If a non-empty parse pattern is provided, but no placeholder characters are specified, the result type will be of type <xref href="System.Reactive.Unit"/>. Otherwise, the output type will be a tuple of the types corresponding to each of the placeholder characters, in order of their appearance in the parse pattern.

| Pattern | Description                                                                             |
| ------- | --------------------------------------------------------------------------------------- |
| `%B`    | Match an unsigned 8-bit integer ([byte](xref:System.Byte)).                             |
| `%h`    | Match a signed 16-bit integer ([short](xref:System.Int16)).                             |
| `%H`    | Match an unsigned 16-bit integer ([ushort](xref:System.UInt16)).                        |
| `%i`    | Match a signed 32-bit integer ([int](xref:System.Int32)).                               |
| `%I`    | Match an unsigned 32-bit integer ([uint](xref:System.UInt32)).                          |
| `%l`    | Match a signed 64-bit integer ([long](xref:System.Int64)).                              |
| `%L`    | Match an unsigned 64-bit integer ([ulong](xref:System.UInt64)).                         |
| `%f`    | Match a single-precision floating-point number ([float](xref:System.Single)).           |
| `%d`    | Match a double-precision floating-point number ([double](xref:System.Double)).          |
| `%b`    | Match a Boolean (`true` or `false`) value ([bool](xref:System.Boolean)).                |
| `%c`    | Match a single character as a UTF-16 code unit ([char](xref:System.Char)).              |
| `%s`    | Match a text fragment using UTF-16 encoding ([string](xref:System.String)).             |
| `%t`    | Match a timestamp measured relative to UTC time (<xref href="System.DateTimeOffset"/>). |
| `%T`    | Match a time interval (<xref href="System.TimeSpan"/>).                                 |

> [!Warning]
> The parse pattern is a regular expression string and certain characters are reserved as special tokens, such as parentheses. It is possible to use these special characters by prefixing them with a backslash (e.g. `\(` for a left parentheses).
