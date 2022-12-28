---
uid: expressions-workflowinput
title: "WorkflowInput"
---

The `WorkflowInput` operator is used inside nested workflows to route input arguments from the outside. The type of the input sequence and its behavior is dependent on the exact operator in which they are nested. Each `WorkflowInput` is uniquely numbered starting from `Source1`.

> [!Warning]
> The numbering of the `WorkfklowInput` nodes usually reflects the order of arguments in the outer operator, but this is not always required. In fact, how many input arguments are available in the nested workflow is entirely dependent on the nesting operator.
