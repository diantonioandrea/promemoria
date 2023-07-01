# promemoria's help

from colorama import Fore, Style


def help() -> str:
    """
    Returns the help string.
    """
    spaces = " " * 4
    introduction: str = "Available commands."
    introduction += "\n" + "-" * len(introduction)

    # new.
    cmdNew: str = Style.BRIGHT + "new " + Style.RESET_ALL
    cmdNew += Style.DIM + "Creates a new reminder" + Style.RESET_ALL

    cmdNew += "\n" + spaces + Fore.RED + Style.BRIGHT + "-t " + Style.RESET_ALL
    cmdNew += Style.DIM + "title, string." + Style.RESET_ALL

    cmdNew += "\n" + spaces + Style.BRIGHT + "-de " + Style.RESET_ALL
    cmdNew += Style.DIM + "description, string. " + Style.RESET_ALL

    cmdNew += "\n" + spaces + Style.BRIGHT + "-da " + Style.RESET_ALL
    cmdNew += Style.DIM + "date, string." + Style.RESET_ALL

    cmdNew += "\n" + spaces + Style.BRIGHT + "-p " + Style.RESET_ALL
    cmdNew += Style.DIM + "priority, integer, [1-3]." + Style.RESET_ALL

    # delete.
    cmdDelete: str = Style.BRIGHT + "delete " + Style.RESET_ALL
    cmdDelete += Style.DIM + "Deletes the specified reminder" + Style.RESET_ALL

    cmdDelete += "\n" + spaces + Fore.RED + Style.BRIGHT + "-i " + Style.RESET_ALL
    cmdDelete += Style.DIM + "index, integer." + Style.RESET_ALL

    # toggle.
    cmdToggle: str = Style.BRIGHT + "toggle " + Style.RESET_ALL
    cmdToggle += Style.DIM + "Toggles the specified reminder" + Style.RESET_ALL

    cmdToggle += "\n" + spaces + Fore.RED + Style.BRIGHT + "-i " + Style.RESET_ALL
    cmdToggle += Style.DIM + "index, integer." + Style.RESET_ALL

    # clear.
    cmdClear: str = Style.BRIGHT + "toggle " + Style.RESET_ALL
    cmdClear += Style.DIM + "Deletes every reminder" + Style.RESET_ALL

    # Full help.
    entries: list[str] = [introduction, cmdNew, cmdDelete, cmdToggle, cmdClear]
    return "\n\n".join(entries)
