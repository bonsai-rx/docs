---
uid: editor
---

# Workflow Editor

When Bonsai starts you will be taken directly to the workflow editor. This is where you can create, configure, and run Bonsai workflows. The editor is composed of three main panels: the [`Toolbox`](#toolbox), the [`Workflow`](#workflow), and [`Properties`](#properties). These are described in more detail below.

![The Bonsai workflow editor](~/images/editor.png)

## Toolbox

The `Toolbox` allows you to search for available operators to place in the workflow. The listing is organized into six main categories:

| Category                                        | Description                                           |
| :---------------------------------------------: | ----------------------------------------------------- |
| ![Source](~/images/language-source.svg)         | generate event streams from devices or files          |
| ![Transform](~/images/language-transform.svg)   | convert or process individual data items              |
| ![Sink](~/images/language-sink.svg)             | save data or trigger external outputs                 |
| ![Combinator](~/images/language-combinator.svg) | manage control flow or synchronize parallel inputs    |
| ![Workflow](~/images/language-workflow.svg)     | reusable workflow fragments stored in `.bonsai` files |
| ![Subject](~/images/language-subject.svg)       | access named event streams defined in the workflow    |

Operators inside each major category are further organized by namespaces linked to the packages you have installed. The name of each namespace can give you a hint about what kind of operations or devices can be accessed inside (e.g. the [`Audio`](xref:Bonsai.Audio) namespace provides access to audio capture devices or WAV file readers).

Once you have found which operator you want to insert, you can place it by double-clicking, dragging it to the workflow or alternatively right-clicking and selecting a specific placement option. See the [Commands and Shortcuts](#commands-and-shortcuts) section for more information.

### Search Operators

Another way to quickly find operators is to use the `Search` textbox. Any text inserted here is matched against available operators, subjects, or namespaces for a match in any order. This means you can search not only for a specific operator name but also by category names to locate all the operators in a namespace (e.g. try typing `Arduino`).

> [!Tip]
> You can directly type and search for operator names when the `Workflow` panel has the input focus. This allows you to simply start typing an operator name and directly select which operator you want with the up/down arrow keys. Once you have the right operator, press the `Enter` key to place it. You can repeat the process multiple times to very quickly chain a sequence of operators.

Another useful function of the `Search` textbox is to find existing instances of the selected toolbox operator in the workflow. Once you select an operator in the toolbox, you can use the `Find Next` or `Find Previous` commands to jump into the next instance of the operator, subject, or workflow extension, starting from the current cursor position.

> [!Tip]
> You can browse through the reference documentation to learn more about each operator in the `Toolbox` by pressing `F1` or selecting `View Help` from the context menu.

## Workflow

The `Workflow` panel is where you combine different operators together to create data processing pipelines. Each operator is represented by a circular node. Nodes can be connected together, forming a directed feedforward graph from left to right. Connections going into a node indicate which operators that node subscribes to (see the [Language Guide](xref:observables) for an extended discussion).

The most useful action to learn your way around the `Workflow` panel is right-clicking. This will bring up the context menu for the specific node you selected, or a list of possible actions you can do with the current selection.

![The workflow context menu](~/images/editor-contextmenu.png)

If only one node is selected, the `Output` menu item will display the type of the elements emitted by that operator sequence.

> [!Tip]
> If the output of an operator is a complex type, you can inspect its public data members. Clicking on any of the sub-items will automatically place a new [`MemberSelector`](xref:Bonsai.Expressions.MemberSelectorBuilder) operator to pick the specified data member from the output of the node.

The context menu also allows you to externalize public properties of the operator as explicit nodes in the workflow using the `Externalize Property` drop-down menu. Once a property is externalized, you can connect other nodes in the workflow to it so you can change the value of the property dynamically (see the [Property Mapping](xref:property-mapping) section for more information).

Finally, it is possible to group nodes, both for organizing large workflows, and to define [higher-order operators](xref:higher-order). The most basic grouping is the [`GroupWorkflow`](xref:Bonsai.Expressions.GroupWorkflowBuilder) which allows you to encapsulate a workflow fragment inside a single node. Any group can be assigned a `Name` for ease of reference and a `Description` for documentation. Any named properties which are externalized from nodes inside the group will be shown as properties of the group node itself on the top-level workflow.

> [!Note]
> You can use `GroupWorkflow` nodes to document your workflow by adding names and descriptions inline with operator chains. These can help readability of a workflow and no additional processing cost is incurred by the use of `GroupWorkflow` nodes.

### Type Visualizers

Type visualizers allow you to inspect online the data that is generated from a specific node during the execution of the workflow. They are useful to visualize the result of specific operations or to debug the behaviour of the workflow itself.

![Example of image type visualizers](~/images/editor-visualizers.png)

#### Assigning visualizers

Types can have more than one visualizer. You can choose the active type visualizer for a specific operator by right-clicking on the corresponding node and selecting from the available options in the `Show Visualizer` menu.

![Select visualizer](~/images/editor-assignvisualizer.png)

For example, image streams can be displayed on the screen using the default image visualizer, but you can also select the text visualizer to inspect image parameters such as size, or pixel bit depth. New visualizers can be added by installing new packages.

#### Visualizer layout settings

If you leave one or more visualizers open when you stop the workflow, the editor will memorize the position and size of each active window. When you run the workflow again, the same visualizer windows will be opened following the memorized layout. These settings are stored in a `.layout` file which is saved side by side with the workflow so they will persist between editor sessions.

> [!Tip]
> Many visualizers allow you to access more detailed information or advanced configuration parameters by right-clicking on the visualizer window.

### Workflow Extensions

You can create and save workflow extensions by selecting one or more nodes and clicking the `Save Workflow As...` button in the context menu.

Workflow extensions are a powerful way to reuse common workflow patterns across a large project. When you save a new extension it will immediately show up in the `Toolbox` panel for placement. Placing a workflow extension will create a new [`IncludeWorkflow`](xref:Bonsai.Expressions.IncludeWorkflowBuilder) operator pointing to the saved workflow. You can place an extension multiple times in the same workflow.

> [!Tip]
> Like other groups, any named properties which are externalized from nodes inside the `IncludeWorkflow` will be shown as properties of the include node itself. These properties can have different values across different instances of the same workflow extension, and will be saved as part of the top-level workflow.

All included workflow extensions are read-only, meaning that you cannot change the internal structure of the extension once it is loaded into the workflow, only its properties. If you want to change the implementation of the extension you need to first `Ungroup` the `IncludeWorkflow` operator. This will make a copy of the included workflow and place it inside a [`GroupWorkflow`](xref:Bonsai.Expressions.GroupWorkflowBuilder). From there you will be able to modify the internal implementation at will. After you have changed the structure, you can save the extension again using `Save Workflow As...`.

> [!Warning]
> When you change the structure of an included workflow and save it over the original file, all references to that workflow extension will be automatically reloaded and updated. This ensures that all references to the same extension remain consistent throughout.

## Properties

Each operator exposes a set of configuration properties that parameterize the operator's behaviour (e.g., the [`Timer`](xref:Bonsai.Reactive.Timer) operator exposes the period between generated values, whereas an image [`Threshold`](xref:Bonsai.Vision.Threshold) exposes the brightness cutoff value applied to individual pixels).

The `Properties` panel will display all the configuration properties which are available for the currently selected operator. A summary description of the currently selected property can be found in the textbox at the bottom of the panel. Similarly, a description of the behaviour of the currently selected operator itself is shown at the top of the panel.

Most properties can be configured simply by changing the text value in the corresponding row of the property grid. Some properties have further specialized editors which can be accessed by clicking the drop-down or dialog button which will be displayed to the right of the property text.

> [!Note]
> Some operators have even more specialized editor windows such as camera configuration dialogs or media player controls. If such property pages exist for the currently selected operator, the small `Property Pages` button (<img src="~/images/propertypages.png" />) above the property grid will become active.

## Actions and Shortcuts

Below is a summary of the most used action and shortcuts in the workflow editor:

| Action | Point-and-click | Keyboard Shortcuts/Modifiers |
| ------------- | --------------- | ------------- |
| Run the workflow | In the `Toolbar` Panel:<br>Click the arrow `Start` button | `F5`  |
| Stop the workflow | In the `Toolbar` Panel:<br>Click the square `Stop` button | `Shift`+`F5`|
| Insert an operator | In the `Toolbox` panel, choose any of these options: <li>Select the operator, drag-and-drop to the `Workflow` panel</li><li>Right-click the operator,  select either of the `Insert` options</li><li>Double-click the operator</li> <br> By default the operator will be placed after a node that is selected in the `Workflow` panel. If a connection can be formed, the two nodes will be connected. <br><br>To insert the operator before a selected node, hold down the `Shift` key together with any of the above actions. | Insert after: `Enter` <br> Insert before: `Shift`+`Enter` |
| Remove an operator | In the `Workflow` panel:<br>Right-click the operator,  select `Remove` | `Delete` |
| Copy-paste an operator | In the `Workflow` panel: <br>Right-click the operator, select `Copy`. Right click another node or anywhere else in the panel, select `Paste`. |Copy: `Ctrl`+`C` <br> Paste after: `Ctrl`+`V`<br> Paste before: `Shift`+`Ctrl`+`V`| 
| Create a branch | In the `Toolbox` panel: <br> With a node already selected in the `Workflow` panel,  right-click the operator and select the `Create Branch` option. | Use `Alt` with any of the existing shortcuts eg. `Alt`+ `Ctrl` + `V`| 
| Create a connection | In the `Workflow` panel: <li> Right-click the source node, select the `Create Connection` option and left-click on the target node <li> Drag the source node and drop it on the target node | N.A. | 
| Remove a connection | In the `Workflow` panel: <br> Right-click the source node, select the `Remove Connection` option and left-click on the target node  | Hold down `Shift` while dragging the source node to the target node.| 
| Select multiple nodes | In the `Workflow` panel: <br> Click on an empty space and drag a box around the nodes to be selected. | <li> While holding the `Shift` key, navigate around the nodes to be selected with the arrow keys.<li>Hold down `Ctrl` while clicking on a node to add/remove it from the current selection.|
| Open type visualizer | In the `Workflow` panel: <li> Double-click on the target node  <li>Right-click on the target node and select a visualizer from the `Show Visualizer` dropdown <br><br> This action is only availiable when the workflow is running. | Press `Enter` while the target node is selected.|  
| Group operators | In the `Workflow` panel: <br> Right-click on a multi-node selection and select a group type from the `Group` dropdown | Select all the nodes to group and press `Ctrl`+`G` to create a nested workflow. |  
| Open operator editor or group workflow | In the `Workflow` panel: <li> When workflow is not running - double-click.<li>When workflow is running - `Ctrl` + double-click. | When workflow is not running:<br>`Enter`<br>When workflow is running:`Ctrl`+`Enter` |  
| Ungroup node group | In the `Workflow` panel: <br> Right-click on the group node and select the `Ungroup` option | `Ctrl`+`Shift`+`G` |  
| Open context menu| In the `Workflow` panel: <br> Right-click any node, multi-node selection or empty space. | `Shift`+`F10` |  

> [!Note]
> Many operations can be performed on multi-node selections (e.g., delete, create connections, create a node group, etc.).

> [!Note]
> You can change the type of an existing group simply by right-clicking on the group node and selecting a different type from the `Group` dropdown.

> [!Note]
> Depending on what is currently selected, the context menu may show different available actions.