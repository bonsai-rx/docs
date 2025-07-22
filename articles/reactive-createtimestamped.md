---
uid: reactive-createtimestamped
title: CreateTimestamped
---

![Marble diagram](~/images/reactive-createtimestamped.svg)

`CreateTimestamped` is used primarily to create a sequence of <xref href="System.Reactive.Timestamped`1"/> values for downstream operators, when timestamps have been extracted from other sources. Alternatively, `CreateTimestamped` can be used to preserve the value of a timestamp during post-processing operations. 

### Example

Use `CreateTimestamped` to carry forward and preserve a timestamp value during post-processing.

:::workflow
![CreateTimestamped Example](~/workflows/reactive-createtimestamped-example.bonsai)
:::