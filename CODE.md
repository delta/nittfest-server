# GithubActions

# Workflow
* on: [pull_request, push] to main: This workflow will work whenever someone push or , make a pull request main branch.
* In the steps we are:
    * if pull_request
        * Checks code formatting.
        * Checks for linting - errors.
        * Checks all test - cases
    * if push
        * Builds Web - Server.
        * Deploys the changes[here]().


# GitHooks

# Configure git-hooks path
* Run the following command
```
git config core.hooksPath .githooks
```
# Features
* pre - commit
    * Runs Formatter
    * Runs Analyzer

* pre - push
    * Checks for un - committed files
    * Runs Test cases
