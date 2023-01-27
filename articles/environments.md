---
uid: environments
title: "Environments"
---

# Bonsai Environments

By default, Bonsai is installed system-wide and can be used to run any workflow. However, as projects grow, it is common to have to install more packages to access specific functionality.

If you have many projects, it can happen that older projects might require specific package versions which might not be compatible with newer projects, resulting in setups that break when the system-wide installation gets updated.

## Keeping track of project dependencies

Bonsai approaches this problem by supporting the creation of reproducible and self-contained environments. An environment is a self-contained, portable, installation of Bonsai that can be used to run a specific project.

To create a reproducible installation of Bonsai we need a *snapshot* of all the packages required to run the workflows in our project. This way, if another person wants to re-use our project, or if we want to keep track of two separate projects in our local machine, we can be assured we have everything in place.

One way to do this is to copy the entire Bonsai install folder, including the `Packages` folder, into the new location. While this works for isolating the two installations, some packages can take up a lot of disk space and contain a large number of files, which makes it hard to share the snapshot with other people and unfeasible to check into version-control systems.

An alternative way is to store just the contents of the local `Bonsai.config` file, which keeps a record of all currently installed dependencies. You can find this file in the same location of the Bonsai executable (`Bonsai.exe`). If you open this XML config file, you will see that it contains a list of all the `Packages`, `AssemblyReferences`, `AssemblyLocations` and `LibraryFolders` which are currently installed.

Anytime you install or update a package, Bonsai will automatically modify the config file. Crucially, the contents of the `Bonsai.config` file are compared with the current state of the `Packages` folder, and if there are any missing packages the Bonsai bootstrapper will download them automatically to recover the expected state of the installation folder.

## Creating an environment

The easiest way to create a self-contained Bonsai environment is to download the portable version of Bonsai and install the packages which are necessary for a specific project. For example, to share a project that depends on the [`Bonsai.Vision`](xref:Bonsai.Vision) package:

1. Start by downloading the [latest Bonsai portable release](https://github.com/bonsai-rx/bonsai/releases/latest/download/Bonsai.zip).
2. After extracting all the files from the `Bonsai.zip` file, your folder will look like this:

![Portable Bonsai release](~/images/environments-portablerelease.png)

3. Run `Bonsai.exe`. During this first run, Bonsai will bootstrap the core dependencies and create an initial `Bonsai.config` file.
4. Install [`Bonsai.Vision`](xref:Bonsai.Vision) using the [`Package Manager`](xref:packages). The `Bonsai.config` will be modified to specify this package is a new dependency. Any additional dependencies which might be needed for the package to run will also be added.
5. Close Bonsai.

## Deploying your environment

Now that we have a `Bonsai.config` file with all the dependencies needed to run our project, how can we reproduce our installation elsewhere? As we saw in the previous step, when we run `Bonsai.exe` for the first time, the bootstrapper will attempt to download and resolve all the core dependencies. However, if a `Bonsai.config` file is found inside the executable folder, the bootstrapper will instead use those dependencies as targets. Let's test it:

1. Repeat steps 1. and 2. from the previous section
2. This time, before running `Bonsai.exe`, copy your `Bonsai.config` into the folder:

![Unziped Bonsai release with config](~/images/environments-bonsaiconfig.png)

2. Run `Bonsai.exe`.
3. Add a node that depends on the Vision package (e.g. [`CameraCapture`](xref:Bonsai.Vision.CameraCapture)) to verify that the package has been successfully installed.
4. You have now deployed your Bonsai environment!

## Adding local dependencies

There is a second configuration file sitting next to the `Bonsai.config` file. This `NuGet.config` file stores a list of all the remote, and local, NuGet package sources where the [`Package Manager`](xref:packages) should look for new packages.

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

We can also use relative paths if we want to keep package sources relative to the local environment. For instance:

```xml
<add key="LocalPackages" value=".\LocalPackages"/>
```

Finally, `NuGet.config` files can be deployed hierarchically. You can have other `NuGet.config` files located higher in the file system to specify package sources that should be shared across multiple projects or specific for the local machine. You can find more information about this and other settings in the [Common NuGet configurations](https://learn.microsoft.com/en-us/nuget/consume-packages/configuring-nuget-behavior) documentation page.

## Version control and "one-click" Bonsai deployment

Now that we know how to create and reuse Bonsai environments, we will show you one way to streamline this whole process.

1. Create the `Bonsai.config` and, if necessary, modify your `NuGet.config` files.
2. Open a new folder and add these two files to it.
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

6. You can now simply share this folder with another user who will be able to easily install your current Bonsai dependencies by running the `Setup.cmd` or `Setup.ps1` file.

As a final bonus, since all these files are encoded as text, they are easily version controlled using a distributed version control system such as [`git`](https://git-scm.com/). Because of this, we often keep this folder inside our project repository and keep updating it with new dependencies as the project evolves.

To prevent all installed packages and other binary files from being tracked, you can add the following lines to the `.gitignore` file for convenience:

```
Packages
*.exe
*.exe.settings
```
