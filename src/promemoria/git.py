# Imports Contents from a specific repo as reminders.

import requests
from .reminders import reminder
from .utilities import parser


def gitContents(prompt: list[str]) -> tuple[bool, list[reminder]]:
    """
    Returns a list of contents from a GitHub repo as reminders.
    """

    _, sdOpts, ddOpts = parser(prompt)

    if "r" not in sdOpts:
        return False, []

    try:
        url: str = "https://api.github.com/repos/{}/{}"

        if "pulls" in ddOpts:
            url = url.format(sdOpts["r"], "pulls")

        else:
            url = url.format(sdOpts["r"], "issues")

    except:  # This should be avoided.
        return False, []

    contents: dict = requests.get(url).json()
    reminders: list[reminder] = []

    for content in contents:
        gitContent: dict[str, str] = {}
        gitContent["title"] = content["title"]
        gitContent["description"] = content["url"]

        if "u" not in sdOpts:
            reminders.append(reminder(gitContent, True))

        # Checks assignee.
        else:
            for assignee in content["assignees"]:
                if assignee["login"] == sdOpts["u"]:
                    reminders.append(reminder(gitContent, True))
                    break

    return True, reminders
