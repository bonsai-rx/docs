# Bonsai Documentation

[![](https://img.shields.io/github/actions/workflow/status/bonsai-rx/docs/build.yml?branch=main&style=flat-square&label=Deployment%20status)](https://github.com/bonsai-rx/docs/actions/workflows/build.yml)

This repo contains the technical reference manual for the Bonsai visual programming language, in addition to articles and examples that document the collective knowledge of the Bonsai user community.

> [!NOTE]  
> This repo hosts the documentation for packages in the Bonsai standard library. Documentation for other Bonsai packages is hosted from each package repo.

Documentation is built using `docfx`, a static site generator that automatically generates API documentation for .NET projects, and deployed using GitHub Actions on GitHub Pages.

We welcome all contributions! For more information please refer to our [Contribution Guide](https://bonsai-rx.org/contribute/).

# Quick start guide for contributing to documentation

These instructions apply to repos that already have a docfx website created.

1. Fork the repository you want to contribute documentation to. 
2. Ensure that you are working off the `main` branch in your fork and create a descriptively named branch for each article/issue that you want to work on.
3. Download and install dotnet (https://dotnet.microsoft.com/en-us/download)
4. Restore `docfx` by running
```powershell
dotnet tool restore
```
5. From a terminal window, use the command `dotnet docfx --serve` to generate a local preview of the documentation website as you are making changes.
6. When you are ready to have your contribution reviewed, commit your edits to the appropriate branch of your fork and create a pull request to merge that branch with the `main` branch of the original repo.
7. Community maintainers will be assigned to review the PR and will conduct the final review and quality control check. If the contribution passes this final step, the PR to merge with `main` will be approved and the contribution will be published.

For more info, check out the [Documentation with docfx](https://bonsai-rx.org/docs/articles/documentation-docfx.html) and [Documentation Style Guide](https://bonsai-rx.org/docs/articles/documentation-style-guide.html) articles.
