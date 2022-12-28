---
uid: property-mapping
title: "Property Mapping"
---

# Property Mapping

Each Bonsai operator exposes a set of configuration properties that allow you to parameterize that operator's behaviour. These parameters can be configured manually from the editor `Properties` panel. However, there are times when you may need to map the properties of an operator dynamically from the output of other observable sequences.

As an example, imagine you wanted to continuously playback a sound WAV file to the speakers at a specified volume level. You might design a workflow that looks like the following:

![WAV file playback](~/images/language-wavplayback.svg)

Using the [`ConvertScale`](xref:Bonsai.Dsp.ConvertScale) operator you could set the volume manually by changing its [`Scale`](xref:Bonsai.Dsp.ConvertScale.Scale) parameter.

Now consider a variation of this workflow where the playback volume needs to be modulated continuously depending on some other variable, for example the horizontal position of the mouse cursor as it moves across the screen.

A simple way to compute the desired scale value would be to rescale the X coordinate of mouse movements to a range between zero and one:

![Rescaled mouse position](~/images/language-mouserescale.svg)

However, how would you now connect the sequence of scale values computed from the mouse position to changes in the [`Scale`](xref:Bonsai.Dsp.ConvertScale.Scale) property of the [`ConvertScale`](xref:Bonsai.Dsp.ConvertScale) node?

Property mapping operators allow you to do exactly this. They are operators that take a single input sequence and react to notifications from that sequence by changing the values of the specified properties in the *subsequent* node. There are three types of property mapping operators, described below.

| Mapping Type | Description |
| :----------: | ----------- |
| ![Externalized mapping](~/images/language-externalizedmapping.svg) | Externalize one or more operator properties. The properties can be optionally named and will show up in the `Properties` panel for node groups. |
| ![Property mapping](~/images/language-propertymapping.svg) | Map multiple properties simultaneously. Individual members of input data items can be mapped to different properties in the target node. |
| ![Input mapping](~/images/language-inputmapping.svg) | Map multiple properties synchronized with input notifications. Same as above, but property changes are applied only when a notification is transmitted to the target node. |

## Externalized properties

The [ExternalizedMapping](xref:Bonsai.Expressions.ExternalizedMappingBuilder) operator allows you to create externalized properties. The easiest way to initialize the mapping is from the right-click context menu when a single node is selected. Selecting a property from this menu will create or update the externalized mapping node. Multiple properties can be externalized from the same node.

![Externalized property](~/images/language-externalizedproperty.png)

[!include[ExternalizedMapping](~/articles/expressions-externalizedmapping.md)]

## Mapping a sequence to a property

After an operator property has been externalized, you can connect any sequence which is compatible with the data type of the property to the mapping node. When a connection to a source sequence is established, the externalized property will be promoted to a [`PropertyMapping`](xref:Bonsai.Expressions.PropertyMappingBuilder) operator.

Now every time the source sequence emits a new notification, the mapping operator will react by changing the target property to the incoming value.

![Rescale WAV playback with mouse position](~/images/language-wavplayback-mapping.svg)

[!include[PropertyMapping](~/articles/expressions-propertymapping.md)]

## Mapping multiple properties

[!include[PropertyMappingMultiple](~/articles/expressions-propertymapping-multiple.md)]

## Mapping properties synchronously

Sometimes you need to synchronize property updates with the data flow, i.e. you do not want the property mapping operator to change the property values outside of notifications emitted by the source sequence.

For example, imagine a transform operator which is converting a source sequence from one format to another, where the format specification is given by a set of operator properties. You may need the target format to change dynamically from time to time, but you may also need to guarantee that parts of the format specification do not change while the operator was converting some other input. The [`InputMapping`](xref:Bonsai.Expressions.InputMappingBuilder) operator allows you to do this by synchronizing property updates with input notifications.

[!include[InputMapping](~/articles/expressions-inputmapping.md)]