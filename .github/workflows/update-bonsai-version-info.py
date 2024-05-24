#!/usr/bin/env python3
import os
import re

import gha

TEMPLATE_PATH = ".github/workflows/version-info-template.md"
INSTALLATION_ARTICLE_PATH = "articles/installation.md"

project_url_base = "https://github.com/bonsai-rx/bonsai/"

#==================================================================================================
# Get inputs
#==================================================================================================
def get_environment_variable(name) -> str:
    ret = os.getenv(name)

    if ret is None or ret == '':
        gha.print_error(f"Missing required parameter '{name}'")
        return ''

    return ret

workflow_dispatch_version = get_environment_variable('workflow_dispatch_version')

# Handle forks for testing purposes
if os.getenv('is_canonical_docs_repo') != 'true':
    project_fork_url = get_environment_variable('project_fork_url')
    project_url_base = project_fork_url.removesuffix('.git')
    if project_url_base[-1] != '/':
        project_url_base += '/'

gha.fail_if_errors()

#==================================================================================================
# Populate template
#==================================================================================================

version_info = ""
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    version_info = f.read()

version_info = version_info.replace("$VERSION$", workflow_dispatch_version)
version_info = version_info.replace("$PROJECT_URL_BASE$", project_url_base)

#==================================================================================================
# Update article
#==================================================================================================

article = ""
with open(INSTALLATION_ARTICLE_PATH, 'r', encoding='utf-8') as f:
    article = f.read()

def replace_function(match):
    return f"{match.group(1)}{version_info}{match.group(3)}"

(article, replacement_count) = re.subn(
    r'(<!-- \[RELEASE_INFO\].+?-->\r?\n)(.+)(<!-- \[/RELEASE_INFO\] -->)',
    replace_function,
    article,
    1,
    re.DOTALL
)

if replacement_count != 1:
    gha.print_error(f"Failed to find the RELEASE_INFO block within '{INSTALLATION_ARTICLE_PATH}'.")
    gha.fail_if_errors()

with open(INSTALLATION_ARTICLE_PATH, 'w',encoding='utf-8') as f:
    f.write(article)

print(f"Bonsai release info in '{INSTALLATION_ARTICLE_PATH}' updated to {workflow_dispatch_version}.")
