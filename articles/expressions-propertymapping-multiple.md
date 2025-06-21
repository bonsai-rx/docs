---
uid: expressions-propertymapping-multiple
title: "PropertyMappingMultiple"
---

Multiple properties can be mapped simultaneously from the same source sequence when using [`PropertyMapping`](xref:Bonsai.Expressions.PropertyMappingBuilder). You can select which properties to map by using the editors available in the property grid. For each mapped property you must specify a source selector, i.e. an expression specifying which members of the input data type are used to assign values to the mapped property.

> [!Note]
> If the type of the selected member does not match the type of the property, a conversion is attempted. If no compatible conversion is available, the compiler checks whether it is possible to construct the corresponding data type from the selected members. For example, it would be possible to map to a [`Point`](xref:OpenCV.Net.Point) type by selecting two numeric values from the source sequence. In this case, the values would be used to construct a new point instance by assigning them to the X and Y parameters of the type constructor.

In each property mapping operator, all mapped properties are updated at the same time every time the source sequence sends out a new value. It is also possible to connect property mapping operators to multiple target nodes.