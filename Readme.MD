> Generate a URL for opening a new GitHub issue with prefilled title, body, and other fields

Inspired by Sindre Sorhus' [new-github-issue-url](https://github.com/sindresorhus/new-github-issue-url)

# Usage

```python
from new_github_issue_url_py import IssueUrl

options = {
    "user": 'YOUR_USERNAME',
    "repo": 'YOUR_REPO',
    "title": "The issue title",
    "body": 'The issue body',
}

issue_url = IssueUrl(options)

issue_url.opn()

[Try the URL](https://github.com/aligoren/new-github-issue-url-py/issues/new?user=aligoren&repo=new-github-issue-url-py&title=I%27m+just+a+human&body=%0A%0A%0A---%0AI%27m+a+human.+Please+be+nice.)

*(Don't click the "Submit new issue" button!)*
```

# API

### IssueUrl(options)

Gives a dict

#### options

Type: `dict`

You are required to either specify the `repoUrl` option or both the `user` and `repo` options.

#### repoUrl

Type: `string`

The full URL to the repo.

#### user

Type: `string`

GitHub username or organization.

#### repo

Type: `string`

GitHub repo.

#### repo

Type: `string`

The issue body.

#### title

Type: `string`

The issue title.

#### template

Type: `string`

Use an [issue template](https://help.github.com/articles/manually-creating-a-single-issue-template-for-your-repository/).

For example, if you want to use a template at `ISSUE_TEMPLATE/unicorn.md`, you would specify `unicorn.md` here.

#### labels

Type: `string[]`

The labels for the issue.

*Requires the user to have the permission to add labels.*

#### milestone

Type: `string`

The milestone for the issue.

*Requires the user to have the permission to add labels.*

#### assignee

Type: `string`

The user to assign to the issue.

*Requires the user to have the permission to add labels.*

#### projects

Type: `string[]`

The projects to add the issue to.

The project reference format is `user/<project-number>`, for example, if the URL to the project is `https://github.com/YOUR_USERNAME/some-repo/projects/3`, the project reference would be `some-repo/3`.

*Requires the user to have the permission to add labels.*

#### url

Returns the last URL

Usage: `print(issue_url.url)`

For example: `https://github.com/YOUR_USER/YOUR_REPO/issues/new?title=EXAMPLE+TITLE&body=EXAMPLE%BODY`

#### opn()

Opens the issue URL on the new tab in your default browser.

Usage: `issue_url.opn()`