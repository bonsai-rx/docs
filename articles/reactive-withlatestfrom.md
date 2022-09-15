---
uid: reactive-withlatestfrom
title: WithLatestFrom
---

![Marble diagram](~/images/reactive-withlatestfrom.svg)

The behavior of `WithLatestFrom` is very similar to [`CombineLatest`](xref:Bonsai.Reactive.CombineLatest), but while `CombineLatest` emits a combined value whenever any of the source sequences emits a value, `WithLatestFrom` only emits the combination when the first sequence emits a value (as long as the second sequence has emitted at least one value).
