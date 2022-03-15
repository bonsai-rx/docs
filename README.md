# Bonsai Documentation

This repo contains the technical reference manual for the Bonsai visual programming language, in addition to articles and examples that document the collective knowledge of the Bonsai user community.

# Would you like to contribute to this repo?

## Step-by-step guide to getting started as a contributor

1. Fork the "develop" branch of this repository. 
2. Download and install the latest stable version of [DocFx](https://dotnet.github.io/docfx/index.html) (currently 2.59).
3. In a Windows Powershell, use the command `docfx docfx.json --serve` to generate a local preview of the documentation website.
4. If you are working on multiple articles at once, create a descriptively named branch of your fork of the repo for each article. 
5. When you are ready to have your contribution reviewed, commit your edits to the approriate branch of your fork of the repo and create a PR to merge that branch with the "develop" branch of this original repo. Because the "develop" branch was created explicitly to aid collaboration between contributors, pull requests to this branch will be accepted and merged rapidly (at least once a week). 
6. Once a piece of documentation has been polished, and at least two community members agree that it is ready for a final review, create a pull request to merge with the "main" branch of this repo. At this point, @glopesdev will conduct the final review and quality control check. If the contribution passes this final step, the PR to merge with "main" will be approved and the contribution will be published on the [publicly accessible Bonsai documentation website](https://bonsai-rx.org/docs-wip/).

### Contributor Style Guide 

 - The "develop" branch is specifically created so that contributors can quickly commit drafts of documentation and collaborate with other community members in order to edit and polish documentation contributions. 
 - Place node names inside a pair of backticks (`` ` ``) so that the node names render in code snippet formatting (i.e. `CameraCapture`)
 - When working on an article, first check [the old documentation](https://bonsai-rx.org/docs/) to see what written material might already exist for that topic. 
