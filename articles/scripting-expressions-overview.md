## Expression Language

The `Scripting.Expressions` namespace uses an early version of the [Dynamic LINQ library](https://dynamic-linq.net/) to assemble expression trees directly into the workflow by using a [special syntax](#expression-language).

> [!Note]
> This expression language aims to be a simple and convenient way of writing arithmetical and value manipulation operations without having to create a separate project or manage local extensions, but it is not a complete query or programming language. If you require more elaborate type or value manipulations, please consider writing a custom [scripting extension](xref:scripting-extensions).

### Literals

The expression language supports boolean, integer, real, string, and character literals. Literals are textual representations of constant values and are one of the most important building blocks of an expression.

| Type      | Examples           | Description                                              |
| --------- | -------------------| -------------------------------------------------------- |
| boolean   | `true`<br/>`false` | A [`Boolean`](xref:System.Boolean) value which can be either `true` or `false`. |
| integer   | `0`<br/>`1L`<br/>`2U`<br/>`3UL` | A sequence of digits. The type of an integer literal is [`Int32`](xref:System.Int32) unless a qualifier character is used to specify the type of the integer (`U` - [`UInt32`](xref:System.UInt32), `L` - [`Int64`](xref:System.Int64), `UL` - [`UInt64`](xref:System.UInt64)). |
| real      | `1.0`<br/>`2.25`<br/>`1e10F`<br/>`1.2345E-4` | An integral part followed by a fractional part and/or an exponent. The fractional part is a decimal point followed by one or more digits. The exponent is the letter `e` or `E` followed by an optional `+` or `-` sign followed by one or more digits. The type of a real literal is [`Double`](xref:System.Double) unless the `F` qualifier is used, in which case the type of the literal will be [`Single`](xref:System.Single). |
| string    | `"hello"`<br/>`""`<br/>`"""quoted"""`<br/>`"'"`  | Zero or more characters enclosed in double quotes. A double quote character can be represented inside a string literal using two consecutive double quotes. The type of a string literal is [`String`](xref:System.String). |
| character | `'A'`<br/>`'1'`<br/>`''''`<br/>`'"'` | A single character enclosed in single quotes. A single quote character can be represented inside a character literal using two consecutive single quotes. The type of a character literal is [`Char`](xref:System.Char). |
| null      | `null` | The `null` literal represents a null reference. The type of the `null` literal is [`Object`](xref:System.Object). |

### Types

The expression language defines special keywords representing the primitive types and a small set of accessible types from the `System` namespace of the .NET Framework Base Class Library.

These accessible types can be used to create new values, convert a value to another type, or to call public static methods available from the type class, as detailed in the documentation reference page of each type.

| <div style="width:130px">Type</div>            | Description |
| ---------------------------------------------- | ----------- |
| [`Boolean`](xref:System.Boolean)               | Represents a Boolean (`true` or `false`) value. |
| [`Byte`](xref:System.Byte)                     | Represents an 8-bit unsigned integer. |
| [`Char`](xref:System.Char)                     | Represents a character as a UTF-16 code unit. |
| [`DateTime`](xref:System.DateTime)             | Represents an instant in time, typically expressed as a date and time of day. |
| [`DateTimeOffset`](xref:System.DateTimeOffset) | Represents a point in time, typically expressed as a date and time of day, relative to Coordinated Universal Time (UTC). |
| [`Decimal`](xref:System.Decimal)               | Represents a decimal floating-point number. |
| [`Double`](xref:System.Double)                 | Represents a double-precision floating-point number. |
| [`Guid`](xref:System.Guid)                     | Represents a globally unique identifier (GUID). |
| [`Int16`](xref:System.Int16)                   | Represents a 16-bit signed integer. |
| [`Int32`](xref:System.Int32)                   | Represents a 32-bit signed integer. |
| [`Int64`](xref:System.Int64)                   | Represents a 64-bit signed integer. |
| [`Object`](xref:System.Object)                 | Supports all classes in the .NET class hierarchy and provides low-level services to derived classes. This is the ultimate base class of all .NET classes; it is the root of the type hierarchy. |
| [`SByte`](xref:System.SByte)                   | Represents an 8-bit signed integer. |
| [`Single`](xref:System.Single)                 | Represents a single-precision floating-point number. |
| [`String`](xref:System.String)                 | Represents text as a sequence of UTF-16 code units. |
| [`TimeSpan`](xref:System.TimeSpan)             | Represents a time interval. |
| [`UInt16`](xref:System.UInt16)                 | Represents a 16-bit unsigned integer. |
| [`UInt32`](xref:System.UInt32)                 | Represents a 32-bit unsigned integer. |
| [`UInt64`](xref:System.UInt64)                 | Represents a 64-bit unsigned integer. |
| [`Math`](xref:System.Math)                     | Provides constants and static methods for trigonometric, logarithmic, and other common mathematical functions. |
| [`Convert`](xref:System.Convert)               | Converts a base data type to another base data type. |

> [!Note]
> [Nullable value types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types) can be specified by writing a `?` after the type name. For example, `Int32?` refers to the nullable form of `Int32`.

### Conversions

The expression language allows explicit conversions between value types using the syntax `type(_expr_)` where `type` is one of the [primitive types](#types) listed above, optionally followed by `?`, and `_expr_` is an arbitrary expression, e.g. the expression `Int32(22.5)` will convert the real number `22.5` to an integer with the type `Int32`.

> [!Note]
> This syntax can be used to convert between the nullable and non-nullable forms of any value type.

### Identifiers

When parsing an expression with a single input element, all members in that element are automatically in scope of the expression string, including public fields, public properties, and public methods. This means any specific member on the input can be accessed by writing an identifier corresponding to the name of that member, e.g. `Item1`.

> [!Warning]
> The casing of identifiers is ignored when resolving members, e.g. `item1` or `ITEM1` can both be used to refer to the member `Item1`.

An identifier consists of a letter or underscore followed by any number of letters, digits, or underscores. In order to reference an identifier with the same spelling as a keyword, the identifier must be prefixed with a single `@` character. Some examples of identifiers are `x`, `Hello`, `m_1`, `@true` and `@String`.

> [!Note]
> The special keyword `it` represents the entire input element, and members can be accessed from this special identifier using dot notation, e.g. `it.Item1`.

### Operators

The expression language supports the following operators in order of precedence of the categories indicated in the table, from top to bottom. Operators in the same category have equal precedence.

In the table below, `x`, `y`, and `z` refer to arbitrary expressions, `T` refers to one of the [accessible types](#types), and `m` refers to a member of an expression value (see the section on [identifiers](#identifiers)).

| Category       | <div style="width:100px">Expression</div> | Description |
| -------------- | -------------- | -------------------------------------- |
| Primary        | `x.m`          | Instance field or property access. Any public field or property can be accessed. |
| Primary        | `x.m(...)`     | Instance method invocation. Any public method may be invoked. Overload resolution follows C# rules. |
| Primary        | `x[...]`       | Array or indexer access. Any public indexer, including multi-dimensional indexers, can be accessed. |
| Primary        | `T.m`          | Static field or static property access. Any public field or property can be accessed. |
| Primary        | `T.m(...)`     | Static method invocation. Any public method may be invoked. Overload resolution follows C# rules. |
| Primary        | `T(...)`       | [Explicit conversion](#conversions) or constructor invocation. |
| Primary        | `new(...)`     | [Data object initializer](#data-object-initializers). This syntax can be used to perform dynamic projections. |
| Primary        | `it`           | Current instance access. See the note in the section on [identifiers](#identifiers). |
| Primary        | `iif(x, y, z)` | Conditional expression. Alternate syntax for `x ? y : z`. |
| Unary          | `-x`           | Negation using two's complement. Supported types are `Int32`, `UInt32`, `Int64`, `Decimal`, `Single`, and `Double`. |
| Unary          | `!x`           | Logical negation. Operand must be of type `Boolean`. |
| Multiplicative | `x * y`        | Multiplication. Only primitive numeric types are supported. |
| Multiplicative | `x / y`        | Division. Only primitive numeric types are supported. |
| Multiplicative | `x % y`        | Remainder. Only primitive numeric types are supported. |
| Additive       | `x + y`        | Addition or string concatenation. Performs string concatenation if either operand is of type `String`. Otherwise, performs addition on primitive numeric types only. |
| Additive       | `x - y`        | Subtraction. Only primitive numeric types are supported. |
| Additive       | `x & y`        | String concatenation. Operands must both be of type `String`. |
| Relational     | `x == y`       | Equal. Supported for reference types and any of the primitive types. Comparison with `null` is also supported. |
| Relational     | `x != y`       | Not equal. Supported for reference types and any of the primitive types. Comparison with `null` is also supported. |
| Relational     | `x < y`        | Less than. Supported for all primitive types except `Boolean`, `Object` and `Guid`. |
| Relational     | `x > y`        | Greater than. Supported for all primitive types except `Boolean`, `Object` and `Guid`. |
| Relational     | `x <= y`       | Less than or equal. Supported for all primitive types except `Boolean`, `Object` and `Guid`. |
| Relational     | `x >= y`       | Greater than or equal. Supported for all primitive types except `Boolean`, `Object` and `Guid`. |
| Logical AND    | `x && y`       | Logical AND. Operands must be of type `Boolean`. |
| Logical OR     | `x || y`       | Logical OR. Operands must be of type `Boolean`. |
| Conditional    | `x ? y : z`    | Evaluate `y` if `x` is `true`, otherwise evaluate `z`. |

### Data Object Initializers

The expression language supports creating dynamic data classes using data object initializers. A data object initializer simultaneously specifies a data class and creates a new instance of that class. The specific properties of the data class are inferred from the data object initializer.

The syntax for a data object initializer is identical to a constructor, where each argument represents a property of the data class. For each argument the value must be specified together with an identifier for the property name, separated by the `as` keyword:

```
new(
  Item1 as X,
  Item2 as Y
)
```

The example above projects the two unnamed items of a tuple into a new data object with an `X` and a `Y` property.