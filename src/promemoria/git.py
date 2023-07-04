# Imports Issues from a specific repo as reminders.

import requests
from .reminders import reminder
from .utilities import parser


def gitIssues(prompt: list[str]) -> tuple[bool, list[reminder]]:
    """
    Returns a list of issues from a GitHub repo as reminders.
    """

    _, sdOpts, ddOpts = parser(prompt)

    if "r" not in sdOpts or ("u" not in sdOpts and "all" not in ddOpts):
        return False, []

    try:
        url: str = "https://api.github.com/repos/{}/issues"
        url = url.format(sdOpts["r"])

    except:  # This should be avoided.
        return False, []

    issues: dict = requests.get(url).json()
    reminders: list[reminder] = []

    for issue in issues:
        gitIssue: dict[str, str] = {}
        gitIssue["title"] = issue["title"]
        gitIssue["description"] = issue["url"]

        if "all" in ddOpts:
            reminders.append(reminder(gitIssue))

        # Checks assignee.
        else:
            for assignee in issue["assignees"]:
                if assignee["login"] == sdOpts["u"]:
                    reminders.append(reminder(gitIssue))

    return True, reminders
