from new_github_issue_url import IssueUrl

options = {
    "user": 'aligoren',
    "repo": 'new-github-issue-url-py',
    "title": "I'm just a human",
    "body": '\n\n\n---\nI\'m a human. Please be nice.',
}

issue_url = IssueUrl(options)

issue_url.opn()

# print(issue_url.url)