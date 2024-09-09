# Bonsai Documentation

[![](https://img.shields.io/github/actions/workflow/status/bonsai-rx/docs/build.yml?branch=main&style=flat-square&label=Deployment%20status)](https://github.com/bonsai-rx/docs/actions/workflows/build.yml)

This repo contains the technical reference manual for the Bonsai visual programming language, in addition to articles and examples that document the collective knowledge of the Bonsai user community.

> [!NOTE]  
> This repo hosts the documentation for the base Bonsai library. Documentation for each new Bonsai package will be hosted in its own repo, for instance, https://github.com/bonsai-rx/machinelearning. 

Documentation is built using DocFx, a static site generator that automatically generates API documentation for .NET projects, and deployed using Github Actions on Github Pages.

# Quick start guide for contributing to documentation

These instructions apply to repos that already have a DocFx website created.

1. Fork the repository you want to contribute documentation to. 
2. Ensure that you are working off the `main` branch in your fork and create a descriptively named branch for each article/issue that you want to work on.
3. Download and install the latest stable version of [DocFx](https://dotnet.github.io/docfx/index.html).
4. In a Windows Powershell, use the command `docfx docfx.json --serve` to generate a local preview of the documentation website as you are making changes'
5. When you are ready to have your contribution reviewed, commit your edits to the approriate branch of your fork and create a pull request to merge that branch with the `main` branch of the original repo.
6. Community members will be assigned to review the PR and @glopesdev will conduct the final review and quality control check. If the contribution passes this final step, the PR to merge with `main` will be approved and the contribution will be published.

For a fuller guide on documentation, check out the [package documentation](./articles/package-documentation.md) article.
