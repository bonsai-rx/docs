---
uid: reactive-currentthreadscheduler
title: CurrentThreadScheduler
---

The `CurrentThreadScheduler` operator returns a singleton object that can be used to schedule units of work in the current thread. The action is placed in a queue rather than executing immediately, and will only be called after the current action is complete.

[!include[Schedulers](~/articles/reactive-schedulers.md)]
