---
uid: packages
---

# Package Manager

Bonsai can be extended by installing software packages containing operators designed for specific tasks, such as video processing or OpenGL shaders.

## Install dependencies

When you first run Bonsai, any required packages will be automatically installed. The built-in package manager can then be launched from the start screen to further customize your installation by selecting the option **Manage packages**.

<img alt="The Bonsai package manager screen" src="~/images/packagemanager.png" style="max-height:450px;object-fit:contain" />

Packages that are already installed are indicated by a green check mark in the bottom-right corner of the package icon. To install a new package, select its title or description, then click the `Install` button that appears next to the version number in the right sidebar. You can also search for available packages using the text box in the upper-left corner.

> [!Note]
> If you want to start playing with Bonsai quickly, just download the "Starter Pack" package. This will automatically install all major dependencies used in this guide.

In the `Installed` tab you can browse currently installed packages and optionally uninstall them. You can also select a different version to downgrade or upgrade, then click on the `Update` button to change the installed version. The `Updates` tab will show you which of those packages can be updated to a newer version.

## Configure package sources

The `Settings` button in the upper-right corner (<img src="~/images/cogwheel.png" />) will open a new dialog where you can configure the active package sources. This allows you to specify directly where Bonsai should look for new packages, either online or in your local file system.

> [!Tip]
> Most of the available Bonsai packages can be found in the official package source (`nuget.org`). However, at some point you may want to install your own custom packages, or packages that were shared with you by other means. See the [Extending Bonsai](create-package.md) section for detailed instructions on how to configure local package sources.

When you are done managing your packages, you can click the `Close` button or hit the Escape key to exit the package manager.