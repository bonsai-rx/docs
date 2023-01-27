---
uid: environments
title: "Environments"
---

# Bonsai Environments

By default, Bonsai is installed system-wide and can be used to run any workflow. However, as projects grow, it is common to have to install new packages to access specific functionality, or update the version of existing packages to get the latest bug fixes and patches.

If you have many projects, you might notice that older projects require specific obsolete package versions which are not compatible with newer projects, resulting in setups that break when the system-wide installation gets updated since only one version of the package can be installed at any one time.

Bonsai addresses these problems by supporting the creation of reproducible package environments. An environment is a self-contained, portable, installation of Bonsai that records a *snapshot* of all the packages required to run the workflows in your project. This makes it much easier to share a project with other people, or keep track of multiple separate projects in our local machine, and be assured you always have everything you need in the right place.

## Creating an environment

The key to creating and updating environments is the `Bonsai.config` file, which keeps a record of all currently installed dependencies for a specific Bonsai setup. You can find this file in the same location of the Bonsai executable (`Bonsai.exe`). Anytime you install or update a package, Bonsai will automatically modify the config file.

The contents of the `Bonsai.config` file are compared with the current state of the `Packages` folder when Bonsai starts. If there are any missing packages the Bonsai bootstrapper will download them automatically to recover the expected state of the installation folder.

The easiest way to create a self-contained Bonsai environment is then to download the portable version of Bonsai and install the packages which are necessary for a specific project. For example, to share a project that depends on the [`Vision`](xref:Bonsai.Vision) package:

1. Start by downloading the [latest Bonsai portable release](https://github.com/bonsai-rx/bonsai/releases/latest/download/Bonsai.zip).
2. After extracting all the files from the `Bonsai.zip` file, your folder will look like this:

![Portable Bonsai release](~/images/environments-portablerelease.png)

3. Run `Bonsai.exe`. During this first run, Bonsai will bootstrap the core dependencies and create an initial `Bonsai.config` file.
4. Install the **Bonsai - Vision** package using the [`Package Manager`](xref:packages). The `Bonsai.config` file will be modified to specify this package as a new dependency. Any additional dependencies which might be needed for the package to run will also be added.
5. Close Bonsai.

## Deploying your environment

Now that you have a `Bonsai.config` file with all the dependencies needed to run your project, how can you reproduce this installation elsewhere? As we saw in the previous step, when we run `Bonsai.exe` for the first time, the bootstrapper will attempt to download and resolve all core dependencies.

However, if a `Bonsai.config` file is found inside the executable folder, the bootstrapper will also resolve those dependencies at startup time. We can test this by doing the following:

1. Create a new folder and repeat steps 1. and 2. from the previous section.
2. This time, before running `Bonsai.exe`, copy your `Bonsai.config` into the folder:

![Unziped Bonsai release with config](~/images/environments-bonsaiconfig.png)

2. Run `Bonsai.exe`.
3. Add a node that depends on the Vision package (e.g. [`CameraCapture`](xref:Bonsai.Vision.CameraCapture)) to verify that the package has been successfully installed.

The new folder is now a copy of your previous environment.

## Adding local dependencies

There is a second configuration file located next to the `Bonsai.config` file called `NuGet.config`. This file stores a list of all the remote, and local, NuGet package sources where the [`Package Manager`](xref:packages) should look for new packages.

The `NuGet.config` file can be modified to specify new package sources. For example, you may want to install local NuGet packages as dependencies (e.g. when testing [your own packages](xref:create-package)).

To do this we just need to add new entries in the `NuGet.config` file. For example, to add a new package source named `LocalPackages` pointing to the Desktop folder:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="Gallery" value="Gallery" />
    <add key="Bonsai Packages" value="https://www.myget.org/F/bonsai/api/v3/index.json" />
    <add key="Community Packages" value="https://www.myget.org/F/bonsai-community/api/v3/index.json" />
    <add key="LocalPackages" value="C:\Users\BonsaiUser\Desktop"/>
  </packageSources>
</configuration>
```

You can also use relative paths if you want to keep package sources relative to the local environment. For instance:

```xml
<add key="LocalPackages" value=".\LocalPackages"/>
```

> [!Note]
> `NuGet.config` files can be deployed hierarchically. You can have other `NuGet.config` files located higher in the file system to specify package sources that should be shared across multiple projects or specific for the local machine. For more information on this and other settings see the [Common NuGet configurations](https://learn.microsoft.com/en-us/nuget/consume-packages/configuring-nuget-behavior) documentation page.

## Version control and "one-click" Bonsai deployment

Now that we know how to create and reuse Bonsai environments, we will show you one way to streamline this whole process.

1. Create the `Bonsai.config` and, if necessary, modify your `NuGet.config` files.
2. Create a new folder and add these two files to it.
3. Add the following `PowerShell` script to the folder (e.g.: open a new text file and copy-paste the code) and name it `Setup.ps1`:

```powershell
if (!(Test-Path "./Bonsai.exe")) {
    Invoke-WebRequest "https://github.com/bonsai-rx/bonsai/releases/download/2.7/Bonsai.zip" -OutFile "temp.zip"
    Move-Item -Path "NuGet.config" "temp.config"
    Expand-Archive "temp.zip" -DestinationPath "." -Force
    Move-Item -Path "temp.config" "NuGet.config" -Force
    Remove-Item -Path "temp.zip"
    Remove-Item -Path "Bonsai32.exe"
}
& .\Bonsai.exe --no-editor
```

When executed, this small script will attempt to download a portable version of a Bonsai release, unzip it, and delete all the unnecessary files.

4. Add a second batch command file `Setup.cmd` that targets and runs `Setup.ps1`. It will look this:

```cmd
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

5. Your folder should now contain only four files:

- `Setup.ps1`
- `Setup.cmd`.
- `NuGet.config`
- `Bonsai.config`

You can now simply share this folder with another person who will be able to easily install your current Bonsai dependencies by running the `Setup.cmd` or `Setup.ps1` file.

As a final bonus, since all these files are encoded as text, they are easily version controlled using a distributed version control system such as [`git`](https://git-scm.com/). Because of this, we often keep this folder inside our project repository and keep updating it with new dependencies as the project evolves.

To prevent installed packages and other binary files from being tracked, you can add the following lines to the `.gitignore` file for convenience:

```
Packages
*.exe
*.exe.settings
```
