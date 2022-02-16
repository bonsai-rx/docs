# Bonsai CLI

Bonsai CLI (Command-Line Interface) allows workflows to be launched from the OS command-line tool. In addition to opening workflows with the default graphic interface, the CLI affords other advanced features, that will be covered ahead, such as "no-editor" mode, initialization of variable's values, and specifying layouts.

In the folder of this tutorial, you will be able find an example workflow you should be able to use to replicate the code examples in your setup (myCameraWorkflow.bonsai).

(Tutorial updated to Bonsai v2.6.1)

___

&nbsp;
## Installation and basic use
Bonsai CLI is available after [installing Bonsai](https://bonsai-rx.org/). Before starting, make sure you can able to call ```Bonsai``` from your command line:

```cmd
> pathToBonsaiExe\Bonsai.exe
```
Alternatively, by adding ```pathToBonsaiExe``` to your System Path, simply:

```cmd
> Bonsai
```

This command should open the default Bonsai editor.

___
&nbsp;
## Opening a Workflow

To open an existing workflow, ```myWorkflow.bonsai```, use the sintax:

```cmd
> Bonsai myWorkflow.bonsai
```

##### Example:

```cmd
> Bonsai myCameraWorkflow.bonsai
> Bonsai "C:\Users\User\Desktop\Example\myCameraWorkflow.bonsai"
```
___
&nbsp;
## Starting a Workflow

Additional flags can be used to change the behavior of Bonsai CLI. To launch and start and workflow from the command line we add the ```--start``` flag to the previous command:

```cmd
> Bonsai myWorkflow.bonsai --start
```

##### Example:
```cmd
> Bonsai myCameraWorkflow.bonsai --start
```

___
&nbsp;
## Starting a Workflow without the editor


For some configurations, such as batch processing, the user might not be interested in editing the script and/or seeing the editor. This can be achieved using the ```--no-editor``` flag. Note that the ```--start``` flag behavior is implicit when running with ```--no-editor``` mode.

```cmd
> Bonsai myWorkflow.bonsai --no-editor
```

After starting the program, a Bonsai icon will appear on your system tray that can be used to stop the workflow or open other visualizers.

![SystemTray Example](~/images/SystemTrayBonsai.png)

It is worth noting that only assigned visualizers will be available on this list. 
To assign a visualizer:
1. Open the workflow in editor mode;
2. Right click on top of the node of interest;
3. "Show Visualizer" ➡ Select a visualizer other than "None"

![Select visualizer](~/images/Select_visualizer.png)


##### Example:
```cmd
> Bonsai myCameraWorkflow.bonsai --no-editor
```
___
&nbsp;
## Passing parameter values to workflows


One of the most useful features of the CLI is the ability to, using the same workflow, passing distinct values to different nodes before starting it. Only "externalized properties" can be set from the command line.

##### To externalize a property:
1. Open the workflow in editor mode;
2. Right click on top of the node of interest;
3. "Externalize Property" ➡ Select the property of interest

![Externalize Property Example 1](~/images/extern_prop_example.png)


- You will notice a new node appears with a dashed line connected to the node of interest. No two externalized properties, in the same scope, are allowed to share the same name. Additionally, you can externalized multiple properties from a single node.
- To change the name of the externalized property (usually a good idea), simply edit the "DisplayName" field of the externalized property node.

![Externalize Property Example 2](~/images/extern_prop_example_2.png)

##### Passing values from the command line
To pass values from the command line we use the syntax :


```cmd
> Bonsai myWorkflow.bonsai -p:<propertyName>=<string>
```
You can set properties in nested workflows by using the (dot) notation: (e.g. ```<NestedNodeName.propertyName> = <string> ```)

It is worth noting that the same workflow file can be called/run in parallel with different parameters, allowing for easy batch-processing pipelines!

##### Example:
```cmd
> :: set a single property
> bonsai myCameraWorkflow.bonsai --start -p:"myThr"="100"

> :: set two distinct properties
> bonsai myCameraWorkflow.bonsai --start -p:"myThr"="100" -p:"myMaxVal"="200"

> :: with "--no-editor" mode enabled
> bonsai myCameraWorkflow.bonsai --no-editor -p:"myThr"="100" -p:"myMaxVal"="200"

> :: set a property of a nested workflow node
> bonsai myCameraWorkflow.bonsai --no-editor -p:"myThr"="100" -p:"myMaxVal"="200" -p:"myNestedNode.howToFlip"="Horizontal"
```
___
&nbsp;
## Specifying layout files
As of version 2.6.1, it is possible to specify which layout file to run the workflow with, when using the ```--no-editor mode```. This is especially useful when the same workflow is meant to be run several times in parallel (e.g. multiple identical behavior rigs).

The general syntax is:

```cmd
> Bonsai myWorkflow.bonsai --no-editor --visualizer-layout:myLayout.bonsai.layout
```

Currently, the easiest way to generate multiple layouts, for a given script, is to:
1. Launch a workflow with the editor;
2. Place the windows in the desired place;
3. Save the workflow.
4. The last step will create a layout file with the same name as the workflow which can then be renamed (prevents being overwritten) and used later.



##### Example:
```cmd

> :: run the workflow myCameraWorkflow.bonsai with myCameraWorkflowLayout2.bonsai.layout
> Bonsai myCameraWorkflow.bonsai --no-editor --visualizer-layout:myCameraWorkflowLayout2.bonsai.layout

> :: run the workflow with the previous layout while setting property values
> Bonsai myCameraWorkflow.bonsai --no-editor --visualizer-layout:myCameraWorkflowLayout2.bonsai.layout -p:"myThr"="100" -p:"myMaxVal"="200" -p:"myNestedNode.howToFlip"="Horizontal"

```

___
&nbsp;
## Examples on how to interface with Bonsai CLI from other programming languages

- Python
  - https://groups.google.com/g/bonsai-users/c/L9SAcfWS7Oo/m/ZnYInEmXBQAJ
  - https://github.com/ThomasAkam/Point_Grey_Bonsai_multi_camera_acquisition

- Matlab
  - https://groups.google.com/g/bonsai-users/c/zXS_1MF8nxM/m/DnkJ5UxkAwAJ

___
&nbsp;

## Other available flags
Additional flags are available and can be used in similar fashion to the ones introduced before:

```cmd
> Bonsai myCameraWorkflow.bonsai --FLAG
> Bonsai --FLAG
> Bonsai --FLAG:<"parameterValue">
```

For a brief description:

- ```--property``` - similar to the "-p" syntax for setting parameter values
- ```--editor-scale``` - Scales the editor UI (e.g. ```bonsai --editor-scale:1.3```)
- ```--start-no-debug``` - Starts the script without the debug mode on
- ```--no-boot``` - Launches bonsai without the bootstrapper
- ```--package-manager``` - Opens the package manager
- ```--gallery``` - Opens the gallery
- ```--export-package``` - Exports the current workflow using the export package dialog (must be inside a folder with the same name)
- ```--reload-editor``` - Reloads the editor




