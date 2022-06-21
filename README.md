# Bonsai Documentation

This repo contains the technical reference manual for the Bonsai visual programming language, in addition to articles and examples that document the collective knowledge of the Bonsai user community.

# Would you like to contribute to this repo?

## Step-by-step guide to getting started as a contributor

1. Fork the "develop" branch of this repository. 
2. Download and install the latest stable version of [DocFx](https://dotnet.github.io/docfx/index.html) (currently 2.59).
3. In a Windows Powershell, use the command `docfx docfx.json --serve` to generate a local preview of the documentation website.
4. If you are working on multiple articles at once, create a descriptively named branch of your fork of the repo for each article. 
5. When you are ready to have your contribution reviewed, commit your edits to the approriate branch of your fork of the repo and create a PR to merge that branch with the "develop" branch of this original repo. Because the "develop" branch was created explicitly to aid collaboration between contributors, pull requests to this branch will be accepted and merged rapidly (at least once a week). 
6. Once a piece of documentation has been polished, and at least two community members agree that it is ready for a final review, create a pull request to merge with the "main" branch of this repo. At this point, @glopesdev will conduct the final review and quality control check. If the contribution passes this final step, the PR to merge with "main" will be approved and the contribution will be published on the [publicly accessible Bonsai documentation website](https://bonsai-rx.org/docs-wip/).

## Contributor Style Guide 

### Why use the "develop" branch?

The "develop" branch is specifically created so that contributors can quickly commit drafts of documentation and collaborate with other community members in order to edit and polish documentation contributions. 

### Re-use/update existing documentation

When working on an article, first check [the old documentation](https://bonsai-rx.org/docs/) to see what written material might already exist for that topic. 

### Including figures

To include a figure or image in an article: 
 - save your figure or image as a `.svg` file, naming the file using the pattern `[article filename]-[figure name].svg`
 - add the figure/image to the **images** folder in this repo

### Standard formatting for operators and operator properties

When referring to operators (also known as nodes in Bonsai), place operator names inside a pair of backticks and double stars (``**`Operator_name`**``) so that the node names render as bold text in code snippet formatting (i.e. **`CameraCapture`**). 

When referring to operator properties, simply place the operator property name inside a pair of backticks (`` `Operator_property_name` ``). 

For both operators and operator properties, link the name to the relevant documentation in the code base, using the [markdown syntax for xref in DocFX](https://dotnet.github.io/docfx/tutorial/links_and_cross_references.html). 

For example, the **`DigitalOutput`** node is part of the `Bonsai.Arduino` namespace/package, and contains a property called `PortName`. To reference this specific property you need to specify the full path to it including namespace, operator name and property name, like so: `xref:Bonsai.Arduino.DigitalOutput.PortName`. 

To find out the full path for any node, right-click on the operator of interest in Bonsai and select the option "Go to Definition" or hit F12. The xref will be the namespace + operator name + (optionally) property name.

**Example:**

```markdown
### **Exercise 7:** Control an LED

![Control an LED](../images/acquisition-led.svg)

- Insert a [**`Boolean`**](xref:Bonsai.Expressions.BooleanProperty) source.
- Insert a [**`DigitalOutput`**](xref:Bonsai.Arduino.DigitalOutput) sink.
- Set the [`Pin`](xref:Bonsai.Arduino.DigitalOutput.Pin) property of the [**`DigitalOutput`**](xref:Bonsai.Arduino.DigitalOutput) operator to 13.
- Configure the [`PortName`](xref:Bonsai.Arduino.DigitalOutput.PortName) property.
- Run the workflow and change the [`Value`](xref:Bonsai.Expressions.BooleanProperty.Value) property of the [**`Boolean`**](xref:Bonsai.Expressions.BooleanProperty) operator.
- **Optional:** Use your mouse to control the LED! Replace the [**`Boolean`**](xref:Bonsai.Expressions.BooleanProperty) operator by a `MouseMove` source (hint: use `GreaterThan`, `LessThan`, or equivalent operators to connect one of the mouse axis to [**`DigitalOutput`**](xref:Bonsai.Arduino.DigitalOutput).
```

### How to include and/or reference examples of workflows

To include and/or reference an example workflow in an article of the documentation, first create the example workflow in a Bonsai workflow editor. Then open File -> Export -> Image or use keyboard shortcut Ctrl + Shift + E. Name the example according to the following pattern: `articleFileName_workflowName`. This will export the example workflow as both a `.svg` file and a `.bonsai` file. 

Add the `.svg` file to the **images** folder in this repo, and add the `.bonsai` file to the **workflows** folder in this repo. In the text of the article that includes/references this example workflow, add the `.svg` file as an image and link that image to the `.bonsai` file. 

**Example:**

Assuming you want to include `acquisition-example.bonsai`: 

```markdown
[![Example Workflow](../images/acquisition-example.svg)](../workflows/acquisition-example.bonsai)
```
