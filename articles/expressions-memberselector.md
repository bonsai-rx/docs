---
uid: expressions-memberselector
title: "MemberSelector"
---

The `MemberSelector` operator is used to quickly extract member fields and properties out of the elements of the source sequence. Multiple members can be specified using a comma-separated list in the <xref href="Bonsai.Expressions.MemberSelectorBuilder.Selector"/> property, in which case the output type will be a tuple of all selected member types.

The <xref href="Bonsai.Expressions.MemberSelectorBuilder.TypeMapping"/> property can be used to specify which type conversion to use when chaining the selected members into downstream operators.
