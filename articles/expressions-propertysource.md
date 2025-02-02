Property sources expose a value which can be set from the property grid and also generate an observable sequence that emits a notification whenever the property value changes, starting with the initial property value.

> [!Tip]
> Property sources are commonly used to create new configuration parameters with custom names for nested workflows. To expose and rename a property source, use [`Property Mapping`](xref:property-mapping#externalized-properties) to externalize the property value and set its [`DisplayName`](xref:Bonsai.Expressions.ExternalizedMapping.DisplayName).