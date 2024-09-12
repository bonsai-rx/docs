# Documentation Style Guide

Clear, well-organized documentation helps users understand package functionality, integrate it into their workflows, and troubleshoot effectively.

Through our experience documenting Bonsai, we've established several best practices for presenting information, which are outlined here alongside practical methods for implementation in [docfx](./documentation-docfx.md). This document is intended as a living resource, open to feedback and continuous improvement, rather than a static guide. Click on the `Edit this page` button or raise an issue on the [bonsai-docs](https://github.com/bonsai-rx/docs/issues) repository if you have a suggestion.

## Article organization

In general, we have found that three types of articles, organized into distinct website sections, are sufficient to address the needs of most users and their learning styles.

* Manual - hosts documentation that explains the basic workflow of the package or functions of the various operators.
* Reference - hosts technical documentation for each operator, generated automatically by DocFX from XML comments in source code or supplemented with individual operator articles.
* Tutorials - hosts examples or tutorials for various applications. This section is optional, but valuable for more complicated applications or packages which require operators from other packages for their execution.

To construct these 3 sections:

1) Ensure that the `docs` folder has a `articles` and `tutorials` folder. The `api` folder is automatically generated.
2) For the navigation bar at the top of the website, edit the `docs/toc.yml` file to reflect the location and name of the various folders.

```yml
- name: Manual
  href: articles/
- name: Reference
  href: api/
- name: Tutorials
  href: tutorials/
```
3) Add articles in markdown format to the `Manual` and `Tutorials` folder 
4) Add a toc.yml file to the `Manual` and `Tutorials` folder to generate the table of contents for that section. The `API` toc.yml is generated automatically.
Here is a sample `articles/toc.yml` with a flattened table of content layout (all articles will be visible in the TOC)

```yml
- href: ../index.md                         # Website Getting Started page that points to docs/index.md. Omit for tutorials/toc.yml
- name: LinearDynamicalSystems              # Group Heading (Optional)
- href: lds-overview.md                     # Article filename
- href: lds-installation-guide-windows.md
- href: lds-installation-guide-linux.md
```

Here is a same `toc.yml` but this time with a nested table of content layout (articles will only be visible when group headings are clicked)

```yml
- href: ../index.md                         
- name: LinearDynamicalSystems              
  items:
  - href: lds-overview.md                    
  - href: lds-installation-guide-windows.md
  - href: lds-installation-guide-linux.md
```
> [!TIP]
> Article filenames should be simple and reflect either the article title or operator name. Titles can be omitted as they will be taken from the first `Heading 1` element.

### Manual articles

For the `Manual` section we typically see these elements:

- Getting Started/Landing page - This typically includes a description of what the package does, how to install the package and funding/acknowledgements. 
- Installation Instructions - If a package requires external dependencies or additional configuration it would be helpful to dedicate an extra page to this.
- Workflow Overview - Best illustrated with a flowchart or a basic workflow container 

Beyond that, there are many possible ways to organise the rest of the manual articles depending on the type of package that is being supported. However one approach that we recommend regardless, is to try and write articles for each individual operator. This approach has several advantages:

- individual operator articles can be integrated into the automatically generated `Reference` documentation using docfx's `overwrite` function, allowing for supplemental content like images and workflows.
- These articles can also be combined into larger conceptual guides, providing organizational flexibility.
- Writing individual operator articles ensures complete coverage of all operators.

Creating an individual operator article requires some 
For example, to create an individual operator article for a `PredictPoses` operator that will be included in a "Network Inference" `Manual` article as well as 
as in the automatically generated `Reference` doc:

1) **Create the Operator Article** - `Bonsai_Sleap_PredictPoses.md` article and place it in the `docs\apidoc` folder. To utilize the `overwrite` function, in the markdown file, assign a UID that follows the namespace.operator format. 

```yml
---
uid: Bonsai.Sleap.PredictPoses
---
Write content here.
```

2) Create a `Network-Inference.md` article and place it in the `docs\articles` folder. In the markdown file, include a reference to the individual operator.md file.

```markdown
Other 
[!include[Title](~/apidoc/Bonsai_Sleap_PredictPoses.md)]
```
> [!NOTE]  
> The title is optional.

### Reference articles

A unique 

The advantage of this approach is that documentation for individual operators will be appended to the automatically generated `Reference` API docs. In addition, they will also show up in the Bonsai editor when users right click on individual operators to `View Help`.






### Tutorials/Examples Submodule
For packages with extensive tutorials, a separate repository can be created and imported as a submodule.
This may be especially helpful if they contain multimedia and other large files. 
A tutorial submodule can be added with the following command.

```cmd
git submodule add https://github.com/bonsai-rx/machinelearning-examples
```
In addition, the `docfx.json` file needs to be modified.
For an example of how to setup a Tutorial submodule, refer to https://github.com/bonsai-rx/machinelearning and its submodule https://github.com/bonsai-rx/machinelearning-examples.

## Article Style Guide 

> [!NOTE]  
> When working on an article, first check [the main documentation](https://bonsai-rx.org/docs/) to see what written material might already exist for that topic that could possibly be used as a reference.

With DocFX, articles are written in [Markdown](https://dotnet.github.io/docfx/docs/markdown.html?tabs=linux%2Cdotnet) and rendered with the [Markdig](https://github.com/xoofx/markdig) parsing engine that supports additional markdown extensions. When writing articles, please follow the [MSDN writing tips](https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips). In particular:

- Keep article and section titles short and succinct so that the table of contents that appears on the left and right sidebar are easier to read (and also to assist in machine translation)
- Reuse operator names, properties, and descriptions in the articles and titles (do not use synonyms) so that readers may more easily follow and refer to them.
- Use the imperative style i.e. "Link hardware triggers" rather than "Linking hardware triggers".

### Standard formatting for operators and operator properties

When referring to operators (also known as nodes in Bonsai), place them inside a pair of backticks  (`` `Operator_name` ``). Link the name to the relevant documentation in the code base, using the [markdown syntax for xref in DocFX](https://dotnet.github.io/docfx/tutorial/links_and_cross_references.html). 

For example, the `DigitalOutput` node is part of the `Bonsai.Arduino` namespace/package. To reference this you need to specify the full path to it including namespace, operator name, like so: `xref:Bonsai.Arduino.DigitalOutput`. To find out the full path for any node, right-click on the operator of interest in Bonsai and select the option "Go to Definition" or hit F12. 

When referring to operator properties, simply place the operator property name inside a pair of backticks (`` `Operator_property_name` ``). 

**Example:**

```markdown
### **Exercise 7:** Control an LED
- Insert a [`Boolean`](xref:Bonsai.Expressions.BooleanProperty) source.
- Insert a [`DigitalOutput`](xref:Bonsai.Arduino.DigitalOutput) sink.
- Set the `Pin` property of the [`DigitalOutput`](xref:Bonsai.Arduino.DigitalOutput) operator to 13.
- Configure the `PortName` property.
- Run the workflow and change the `Value` property of the [`Boolean`](xref:Bonsai.Expressions.BooleanProperty) operator.
```

### Bonsai workflows

To include and/or reference an example workflow in an article of the documentation, first create the example workflow in a Bonsai workflow editor and save the workflow as `articleFileName_workflowName`. 
Add the `.bonsai` file to the **workflows** folder in the repo. In the text of the article that includes/references this example workflow, add a workflow container.

**Example:**

Assuming you want to include `custom-pulse-train_send-custom-waveform.bonsai`: 

```markdown
:::workflow
![Send Custom Waveform](../workflows/custom-pulse-train_send-custom-waveform.bonsai)
:::
```

Workflow images are automatically exported as SVGs by the [docfx-tools](https://github.com/bonsai-rx/docfx-tools) submodule. 
If any of the nodes are greyed out in the SVG images when published, then the `config.yml` file in the `.Bonsai` folder needs to be updated.  
For instance, if you used a `KeyDown` operator in your sample Bonsai workflow, the `Bonsai.Windows.Input` package needs to be included.

Navigate to your local Bonsai installation folder, and you will find a `config.yml` that includes the necessary information to copy over to the `config.yml` file in `.bonsai` folder. 
Only copy the lines that reference the package.

### Figures

> [!NOTE]  
> Avoid images/screenshots when possible as they do not display well across light/dark mode and do not scale well across different display sizes and resolutions. See the following sections for alternative ways of creating different content.

To include a figure or image in an article: 

1) Save your figure or image as a `.svg` file, naming the file using the pattern `[article filename]-[figure name].svg`.
2) Add the figure/image to the **images** folder in the repo.
3) Reference the figure in the article with the following code.
4) (Optional) For smaller screenshots, it may help to set a max width so that the fonts do not blow up too much on desktop displays. This can be done by setting a `width` attribute on the img element directly like follows.

**Example:**

```markdown
!['Editor Gallery'](~/images/editor-gallery.png){width=500}
```

### Diagrams and Charts

Use [Mermaid](https://mermaid.js.org/) graphs to visualize flowcharts or pipelines.

**Example:**

````markdown
```mermaid

flowchart LR

    A(["Create Python Runtime"])
    B(["Load LDS Module"])
    C(["Create KF Model"])
    D(["Generate Observations"])
    E(["Perform Inference"])

    A --> B
    B --> C
    C --> D
    D --> E

```
````

```mermaid

flowchart LR
    A(["Create Python Runtime"])
    B(["Load LDS Module"])
    C(["Create KF Model"])
    D(["Generate Observations"])
    E(["Perform Inference"])

    A --> B
    B --> C
    C --> D
    D --> E
```

### Property Tables

Highlight properties to change for a particular application by representing them as [markdown pipe tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables).

**Example:**
``` markdown
| Category          | Property Name       | Value                  | Description                        |    
| ----------------  | ------------------- | ---------------------- | ---------------------------------- | 
|  Pulse Timing     | `PulseTrainDelay`   | 0.0001 - 3600 (secs)   | The delay to start the pulse train.|
|  Pulse Timing     | `PulseTrainDuration`| 0.0001 - 3600 (secs)   | The duration of the pulse train.   |
```

| Category          | Property Name       | Value                  | Description                        |
| ----------------  | ------------------- | ---------------------- | ---------------------------------- | 
|  Pulse Timing     | `PulseTrainDelay`   | 0.0001 - 3600 (secs)   | The delay to start the pulse train.|
|  Pulse Timing     | `PulseTrainDuration`| 0.0001 - 3600 (secs)   | The duration of the pulse train.   |

### Code snippets
Use code blocks to highlight code to run. Enable language specific highlighting by adding a language identifier at the beginning.

````markdown
```powershell
dotnet new tool-manifest 
dotnet tool install --local docfx --version 2.75.3
```
````

### Alerts

Use alerts to alert users to important information. Only use either the `Note` or `Warning` alerts as they do not conflict with the formatting for property names.

**Example:**
```markdown
> [!NOTE]
> Information the user should notice even if skimming.

> [!WARNING]
> Dangerous certain consequences of an action.
```
> [!NOTE]
> Information the user should notice even if skimming.

> [!WARNING]
> Dangerous certain consequences of an action.

### Final Polishing Steps

Delete redundant blank rows in between lines and at the end of the articles. This improves code readability for future contributors.

