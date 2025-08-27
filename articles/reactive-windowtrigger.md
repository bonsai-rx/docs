---
uid: reactive-windowtrigger
title: WindowTrigger
---

![Marble diagram](~/images/reactive-windowtrigger.svg)

`WindowTrigger` groups the notifications of the source sequence into new observable sequences, where the opening of each window is triggered by the notifications of the second sequence. The rules for closing each window can be specified using the <xref href="Bonsai.Reactive.WindowTrigger.Count"/> and <xref href="Bonsai.Reactive.WindowTrigger.TimeSpan"/> properties.

If neither count nor time span are specified, windows will be strictly non-overlapping, with the previous window being closed when a new window is created. In this case, and only this case, the first window is also created immediately at the start of the sequence.

If the `Count` property or the `TimeSpan` property is specified, then a new window is created when the second sequence emits a notification, and it is automatically closed after either the specified number of elements is collected or the specified time span elapses. If a new window is created before the previous window is closed, then window will overlap, and any elements emitted during this period will be included in both windows. If at any moment there is no open window, elements emitted from the source sequence will be dropped.

> [!Note]
> You can manipulate and schedule each of the windows downstream using other higher-order operators such as [**Merge**](xref:Bonsai.Reactive.Merge), [**Concat**](xref:Bonsai.Reactive.Concat) or [**Switch**](xref:Bonsai.Reactive.Switch).

### Example

Use `WindowTrigger` to group elements into zero or more observable sequences based on notifications from a second sequence.

:::workflow
![WindowTrigger Example](../workflows/reactive-windowtrigger-example.bonsai)
:::

### Alternatives

Use [`BufferTrigger`](xref:Bonsai.Reactive.BufferTrigger) instead to group elements into zero or more buffers based on notifications from a second sequence.

Use [`Window`](xref:Bonsai.Reactive.Window) instead if you want to specify a dynamic close condition.