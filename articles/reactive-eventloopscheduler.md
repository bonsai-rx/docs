---
uid: reactive-eventloopscheduler
title: EventLoopScheduler
---

[!include[Schedulers](~/articles/reactive-schedulers.md)]

> [!Important]
> The scheduler object returned by `EventLoopScheduler` needs to be explicitly disposed. Assign the result of this operator to a <xref href="Bonsai.Reactive.ResourceSubject"/> to ensure the dedicated scheduler thread is terminated at the end of the workflow.

:::workflow
![Creating an EventLoopScheduler](~/workflows/reactive-eventloopscheduler-example.bonsai)
:::
