---
uid: reactive-window
title: Window
---

![Marble diagram](~/images/reactive-window.svg)

The `Window` operator groups the notifications of the source sequence into new observable sequences. The opening of each window is triggered by notifications emitted by the second sequence passed to the `Window` node. The nested workflow operation is launched for every new emitted window, and closes that window when a value is emitted.

If a new window is created before the previous window is closed, then window will overlap, and any elements emitted during this period will be included in both windows. If at any moment there is no open window, elements emitted from the source sequence will be dropped.

> [!Note]
> You can manipulate and schedule each of the windows downstream using other higher-order operators such as [`Merge`](xref:Bonsai.Reactive.Merge), [`Concat`](xref:Bonsai.Reactive.Concat) or [`Switch`](xref:Bonsai.Reactive.Switch).

### Example

Use `Window` to group elements into zero or more observable sequences based on notifications from a second sequence as well as the encapsulated workflow.

:::workflow
![Window Example](../workflows/reactive-window-example.bonsai)
:::

### Alternatives

Use [`WindowTrigger`](xref:Bonsai.Reactive.WindowTrigger) instead to group elements into zero or more observable sequences based solely on notifications from a second sequence.