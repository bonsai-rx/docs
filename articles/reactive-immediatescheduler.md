---
uid: reactive-immediatescheduler
title: ImmediateScheduler
---

The `ImmediateScheduler` operator returns a singleton object that can be used to schedule units of work to run immediately on the current thread. If there is a recurrent scheduling call downstream from the work unit, the scheduler may hang indefinitely.

[!include[Schedulers](~/articles/reactive-schedulers.md)]
