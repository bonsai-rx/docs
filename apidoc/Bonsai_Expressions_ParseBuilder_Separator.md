---
uid: Bonsai.Expressions.ParseBuilder.Separator
remarks: *content
---

If both <xref href="Bonsai.Expressions.ParseBuilder.Separator"/> and <xref href="Bonsai.Expressions.ParseBuilder.Pattern"/> are specified, the separator will be used first to split the input strings. Each delimited substring will then be matched against the regular expression specified in the parse pattern. The result will be an array of the output type inferred from the structure of the parse pattern.
