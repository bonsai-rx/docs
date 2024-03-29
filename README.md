# Bonsai Documentation

[![](https://img.shields.io/github/actions/workflow/status/bonsai-rx/docs/build.yml?branch=main&style=flat-square&label=Deployment%20status)](https://github.com/bonsai-rx/docs/actions/workflows/build.yml)

This repo contains the technical reference manual for the Bonsai visual programming language, in addition to articles and examples that document the collective knowledge of the Bonsai user community.

> [!NOTE]  
> This repo hosts the documentation for the base Bonsai library. Documentation for each new Bonsai package will be hosted in its own repo, for instance, https://github.com/bonsai-rx/machinelearning. The instructions below apply to both documentation for the base Bonsai library as well as new packages.

Documentation is built using DocFx, a static site generator that automatically generates API documentation for .NET projects, and deployed using Github Actions on Github Pages.

# Would you like to contribute to documentation?

## Contributing to existing documentation

These instructions apply to repos that already have a DocFx website created.

1. Fork the `main` branch of the repository you want to contribute documentation to.
2. Download and install the latest stable version of [DocFx](https://dotnet.github.io/docfx/index.html) (currently 2.75.3).
3. In a Windows Powershell, use the command `docfx docfx.json --serve` to generate a local preview of the documentation website as you [make changes](#creating-and-editing-articles).

> [!NOTE]  
> Occasionally, we run into weird bugs with the local preview. Check if the error persists by [publishing your fork online](#publishing-to-github-pages)

4. When you are ready to have your contribution reviewed, commit your edits to the approriate branch of your fork and create a pull request to merge that branch with the `main` branch of the original repo.
5. Community members will be assigned to review the PR and @glopesdev will conduct the final review and quality control check. If the contribution passes this final step, the PR to merge with `main` will be approved and the contribution will be published.


## Setting up new documentation

For packages without existing documentation, a new DocFx website needs to be initialized.

1) In Windows Powershell, setup a local installation of DocFx in the repo with the following commands (executed in the root directory of the repo). 

```powershell
dotnet new tool-manifest 
dotnet tool install --local docfx --version 2.75.3
```

2) Create a new `docs` folder to host the documentation files. Navigate to the folder and initialise a new DocFx website with the following command.

```powershell
dotnet docfx init 
```

3) Select these options for the new website.

```powershell
Name (mysite): Bonsai - Package Name
Generate .NET API documentation? [y/n] (y): y
.NET projects location (src): src
Markdown docs location (docs): articles
Enable site search? [y/n] (y): y
Enable PDF? [y/n] (y): n
```
This creates a docfx.json file in the "docs" folder that hosts the configuration options for the website. 

4) Configure docfx.json - the parameters to be changed can be copied over from the docfx.json in a repo that has been recently updated (for instance https://bonsai-rx.org/machinelearning/). 

Add the `filter` attribute to filter out obsolete nodes in the package from the documentation that have been included for compatibility purposes (but are no longer supported).
```yml
"metadata": [
    {
        "filter": "filter.yml"
    }
]
```
Exclude the `filter.yml` from being included in the building of content.

```yml
"build": {
    "content": [
        {
        "exclude": [
            "_site/**",
            "filter.yml"
        ]
        }
    ]
}
```

List any additional files/folders that are to be used in the doc in the `resource` attribute.

```yml
"build": {
    "resource": {
        "files": [
            "logo.svg",
            "favicon.ico",
            "images/**",
            "workflows/**"
        ]
    }
}
```

Add the `overwrite` attribute to enable individual operator articles stored in the `apidocs` folder to be included in articles and API docs.

```yml
"build": {
    "overwrite": [
      {
        "files": [
          "apidoc/**.md"
        ],
        "exclude": [
          "obj/**",
          "_site/**"
        ]
      }
    ],
}
```

Modify the `template` attribute to use the modern template and apply custom templates to enable workflow containers.

```yml
"template": [
    "default",
    "modern",
    "bonsai/template",
    "template"
]
```

Change PackageName and github link to the repo being worked on and add footer information to the `globalMetadata` attribute.

```yml
"globalMetadata": {
    "_appName": "Bonsai - PackageName",
    "_appTitle": "Bonsai.PackageName",
    "_appFooter": "&copy; 2024 Bonsai Foundation CIC and Contributors. Made with <a href=\"https://dotnet.github.io/docfx\">docfx</a>",
    "_gitContribute": {
        "repo": "https://github.com/bonsai-rx/PackageName",
        "branch": "main",
        "apiSpecFolder": "apidoc"
    }
}
```

Enable additional markdig (the default DocFX markdown processor) extensions.

```yml
"build": {
    "markdownEngineProperties": {
        "markdigExtensions": [
        "attributes",
        "customcontainers"
        ]
    }
}
```

Add a `xref` attribute to cross reference operators and properties across the different Bonsai docs websites.

```yml
"build": {
    "xref": [
        "https://bonsai-rx.org/docs/xrefmap.yml",
        "https://horizongir.github.io/reactive/xrefmap.yml"
    ]
}
```

5) In the "docs" folder, create these folders to host various contents that will go into the docs.

```markdown
- articles - markdown files for various articles that will go into the `Manual`.
- apidoc - markdown files for individual Bonsai operators to be included in articles or `Reference`.
- images - images for the website.
- workflows - .bonsai files for example workflows. 
```

6) Copy over these folders/files from a repo that has been recently updated into the root folder of the repo. Amend the files as necessary. 

```markdown
- .github folder - contains a workflows/docs.yml file that is a Github Actions workflow recipe.
    - Make sure that it is updated to the latest version and change the package name parameters.

- .bonsai folder - files necessary to build a Bonsai environment on Github Actions.
    - The config.yml file in the .bonsai folder needs to be amended to include any packages 
    that are necessary for running the SVG export for sample Bonsai workflows (see section below)
    - The new Bonsai package itself does not need to be included.

- .gitignore file - this needs to be updated to ignore workflow files (i.e. .bonsai packages env).
```

7) Copy over these folders/files from a repo that has been recently updated into the "docs" folder.

```markdown
- docs/filter.yml file - filters out obsolete operators from being included in API documentation.
- docs/.gitignore file - filters out the _site folder that is generated during local preview.
- docs/favicon.ico and logo.svg - files for site logo and bookmark icon.
- docs/workflows/.gitignore file - ignores bonsai layout files and svg files.
- docs/build.ps1 file - script  used to export images for sample workflows.
    - amend the line in the file to the new package name and source location.
- docs/template/public folder- contains main.css and main.js which patches in `docfx-tools`.
    - amend main.js to change the github link to the current repository.
```

8) Add the [docfx-tools](https://github.com/bonsai-rx/docfx-tools) submodule. This submodule contains scripts for automating SVG export from Bonsai workflows and patches the DocFx CSS templates to add workflow containers. 

```cmd
git submodule add https://github.com/bonsai-rx/docfx-tools docs/bonsai
```
If the submodule does not show up in your local copy, run these additional commands.

```powershell
git submodule init
git submodule update
```

# Creating and Editing Articles

## Article Organization

### Navigation bar
The navigation bar at the top of the DocFX website should have 2-3 links to the main pages of the website.

* Manual - hosts documentation that explains the basic functions of the various operators in the package.
* Reference - generated automatically by DocFX from XML comments in the Bonsai package source code.
* Tutorials - optional page that would have examples or tutorials for various applications.

To construct the navigation bar, edit the `docs/toc.yml` file to reflect the location and name of the various pages.

```yml
- name: Manual
  href: articles/
- name: Reference
  href: api/
- name: Tutorials
  href: articles/tutorials/
```

### Table of contents
For the `Manual` and `Tutorials` pages of the website, the table of contents is built from a `toc.yml` file located in the respective folders. The table of contents for the API page is generated automatically.

Getting started/Landing page - the first page of the docs website will be an `index.md` file that is located in the `docs` folder. This typically includes a description of what the package does, installation instructions (if not too complicated) and acknowledgements. To make this page the landing page, in the `articles/toc.yml` file, the getting started page should be listed as shown. This step is omitted from the tutorials `toc.yml`.

```yml
- href: ../index.md
```

> [!NOTE]  
> Article names can be omitted as they will be taken from the first `Heading 1` element in the article.

For the rest of the articles, they can be added to the articles folder and referred to as follows.
Article filenames should be simple and reflect either the article title or operator name (if the article is about a specific operator).

```yml
- href: ../index.md
- href: lds-overview.md
```

To organise articles into different sections, simply include a name before the links to the articles that you want to group together. 

```yml
- href: ../index.md
- name: LinearDynamicalSystems
- href: lds-overview.md
- href: lds-installation-guide-windows.md
- href: lds-installation-guide-linux.md
```

> [!NOTE]
> While there is another method of grouping articles together that makes a nested table of contents, we prefer this method as it expands the table of contents so that users can see all the articles at once and get to them quicker.

### Individual Bonsai operator articles
Where possible, documentation should be written for individual Bonsai operators and embedded in the `Manual` articles. The advantage of this approach is that documentation for individual operators will be appended to the automatically generated `Reference` API docs. In addition, they will also show up in the Bonsai editor when users right click on individual operators to `View Help`.

For example, to create documentation for a `PredictPoses` operator that will be included in a `Network Inference` article for the `Bonsai.Sleap` package:

1) Create a `Bonsai_Sleap_PredictPoses.md` article and place it in the `docs\apidoc` folder. In the markdown file, assign a UID that follows the namespace.operator format.

```yml
---
uid: Bonsai.Sleap.PredictPoses
---

Write content here.
```

2) Create a `Network-Inference.md` article and place it in the `docs\articles` folder. In the markdown file, include a reference to the individual operator.md file.

```yml
[!include[Title](~/apidoc/Bonsai_Sleap_PredictPoses.md)]
```
> [!NOTE]  
> The title is optional.

### Tutorials/Examples Submodule
For packages with extensive tutorials, a separate repository can be created and imported as a submodule.
This may be especially helpful if they contain multimedia and other large files. 
A tutorial submodule can be added with the following command.

```cmd
git submodule add https://github.com/bonsai-rx/machinelearning-examples
```
In addition, the `docfx.json` file needs to be modified.
For an example of how to setup a Tutorial submodule, refer to https://github.com/bonsai-rx/machinelearning and its submodule https://github.com/bonsai-rx/machinelearning-examples.

## Contributor Style Guide 

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

# Testing Unpublished Packages
To write documentation for new packages or releases that have not been published to the community, test them in Visual Studio. 
Adapted from https://bonsai-rx.org/docs/articles/create-package.html.

1) Install [Visual Studio](https://www.visualstudio.com/) (the community edition can be installed for free).
2) Install Bonsai VS Extensions. Assuming Bonsai is already installed, from the Windows Start Menu, search for the "Install Bonsai VS Extensions" shortcut and run it.
3) In Visual Studio, open `src/PackageName.sln` in the repo.
4) Press F5 to open the Bonsai editor with the new package added. 
5) From here, you can make Bonsai workflows and save them as per normal.

# Publishing to Github Pages

Although this step is not necessary, it can be helpful if you want to check how your edits look online if the local preview is not working.

1) Setup a new branch called `gh-pages` on your fork of the repository.
2) Go to your repo settings -> `Pages` -> `Build and deployment` - under `Source` select `Deploy from a branch` and make sure `gh-pages` is selected.
3) Commit your edits and push to the `main` branch of your repo fork. 
4) Under the `Actions` tab of your github repo, trigger the `Build docs` workflow manually with the `Run workflow` button. This will build the docs site on the `gh-pages` branch.
5) Once the `Build docs` workflow has been completed, the `pages-build-deployment` workflow will run and publish your forked repo automatically.
7) The URL for the site can be found in your `Pages` section of your repo settings.