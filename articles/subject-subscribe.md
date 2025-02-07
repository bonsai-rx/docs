---
uid: subject-subscribe
title: "SubscribeSubject"
---

The [`SubscribeSubject`] operator is essentially a source which accesses a subject with the specified name, at the same scope level or above, and subscribes to it. The behavior of [`SubscribeSubject`] is defined by the type of the subject which is accessed, and values from the shared underlying sequence will then be passed to any operators downstream from [`SubscribeSubject`], as if these operators were connected to the subject directly.

:::workflow
![SubscribeSubject workflow](~/workflows/language-subject-subscribe.bonsai)
:::

> [!Note]
> If the definition of the underlying subject changes, there is no need to change the [`SubscribeSubject`] as long as the name remains the same.

<!-- Reference-style links -->
[`SubscribeSubject`]: xref:Bonsai.Expressions.SubscribeSubject