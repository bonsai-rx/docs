---
uid: create-env
title: "Creating an environment"
---

# Creating a Bonsai environment


## Keep track of your project dependencies

For some applications, we might want to have a *snapshot* of all the currently installed Bonsai packages in our project. For example, another user might want to re-use our workflows, or we might simply like to keep two projects separated in our local machine. While we could copy the `Packages` folder, in the Bonsai installation folder, some packages can take up a lot of disk space and contain a large number of files.

Fortunately, Bonsai keeps a record of the currently installed dependencies for each Bonsai executable (`Bonsai.exe`). You can find this file in the same folder as your executable under the name `Bonsai.config`. Inside this `XML` file, a list of all the `Packages`, `AssemblyReferences`, `AssemblyLocations` and `LibraryFolders` currently installed can be found.

When you install or update a package, Bonsai will automatically modify this file.

## Creating an environment

The most straightforward way to create a Bonsai environment is to download a clean version of Bonsai and install the packages necessary for a specific project. Let's say I want to share a project that depends on the  [**`Bonsai.Vision`**](xref:Bonsai.Vision) library.

1. We start by downloading a Bonsai release. In this case, We will [use the 2.7 portable release](https://github.com/bonsai-rx/bonsai/releases/download/2.7/Bonsai.zip).
2. After extracting all the files from `Bonsai.zip`, your folder will look like this:
![Unziped Bonsai release](~/images/environment-unziprelease.PNG)
3. Run `Bonsai.exe`. Notice that, after this first run, Bonsai will bootstrap the core dependencies and create an initial `Bonsai.config`.
4. Install [**`Bonsai.Vision`**](xref:Bonsai.Vision) using the [`Package Manager`](https://bonsai-rx.org/docs/articles/packages.html). After this step, a few lines will have been added to `Bonsai.config` that establishes this package as a new dependency. Other sub-dependencies, that might also be needed for the package to run, will also be added.
5. Close Bonsai.

## Deploying your environment

Now that we have a file we all the dependencies needed to run our project, how can we reproduce our installation elsewhere? As we saw in the previous step, when we run `Bonsai.exe` for the first time, the bootstrapper will attempt to download and resolve all the core dependencies. However, if a `Bonsai.config` file is found inside the executable folder, the bootstrapper will instead use those dependencies as targets. Let's test it:

1. Repeat steps 1. and 2. from the previous section
2. This time, before running `Bonsai.exe`, copy your `Bonsai.config` the folder:
![Unziped Bonsai release with config](~/images/environment-bonsaiconfig.PNG)
3. Run `Bonsai.exe`.
4. Add a node that depends on the Vision package (e.g. [**`CameraCapture`**](xref:Bonsai.Vision.CameraCapture)) to verify that the package has been successfully installed.
5. You have now deployed your Bonsai environment!

## Adding local dependencies

You probably noticed that a second configuration file accompanies the `Bonsai.config`. This file, `Nuget.config` keeps a record of all the remote, and local, NuGet package sources that the [`Package Manager`](https://bonsai-rx.org/docs/articles/packages.html) should look for new packages in.

Sometimes, we might need local NuGet packages as dependencies. [For instance, if we generate them ourselves](https://bonsai-rx.org/docs/articles/create-package.html).

We can easily add these directories by appending them to `Nuget.config`. If we want to add a new package source named `LocalPackages`, which sits in the user's desktop, `Nuget.config` would end up looking like this:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
    <packageSources>
        <add key="Gallery" value="Gallery" />
        <add key="Bonsai Packages" value="https://www.myget.org/F/bonsai/api/v3/index.json" />
        <add key="Community Packages" value="https://www.myget.org/F/bonsai-community/api/v3/index.json" />
        <add key="LocalPackages" value="C:\Users\BonsaiUser\Desktop\"/>
    </packageSources>
    </configuration>
```

Should we want to keep it relative to our `Bonsai.exe`, we could simply use relative paths. For instance:

```xml
<add key="LocalPackages" value=".\Packages"/>
```
## Version control and "one-click" Bonsai deployment

Now that we know how to create and reuse Bonsai environments, we will show you one way to streamline this whole process.

1. Create your `Bonsai.Config` and, if necessary, modify your `Nuget.Config` files.
2. Open a new folder and add these two files to it.
3. Add the following `PowerShell` script to the folder (e.g.: open a new text file and copy-paste the code) and name it `setup.ps1`:

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

4. Add a command file (`setup.cmd`) that targets and runs `setup.ps1`. It will look this this:

```cmd
    powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

5. Your folder should now only contain four files

   - `Setup.ps1` and `Setup.cmd`.

   - `Nuget.config`

   - `Bonsai.config`

6. Now you can simply share this folder with another user who will be able to easily install your current Bonsai dependencies.

As a final bonus, since all these files are encoded as text, they are easily versioned using `Git` tools. As a result, we often keep this folder inside our Bonsai project and keep updating it with new dependencies as the project evolves. To prevent all the installed packages and other files from being tracked, we often add the following lines to `.gitignore`:

```
Packages
*.exe
*.exe.settings
```
