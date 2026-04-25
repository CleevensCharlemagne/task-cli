from task_cli import commands

COMMANDS = {
    "add": {
        "func": commands.add_task,
        "types": [str],
    },
    "mark-in-progress": {
        "func": commands.mark_in_progress,
        "types": [int],
    },
    "mark-done": {
        "func": commands.mark_done,
        "types": [int],
    },
    "update": {
        "func": commands.update,
        "types": [int, str],
    },
    "delete": {
        "func": commands.delete,
        "types": [int],
    },
    "list": {
        "func": commands.show,
        "types": [],  # optional param handled separately
    },
}

def dispatch(args, storage):
    if not args:
        print("No command provided")
        return

    command = args[0]
    params = args[1:]

    if command not in COMMANDS:
        print("Unknown command")
        return

    entry = COMMANDS[command]
    func = entry["func"]
    types = entry["types"]

    try:
        # Convert parameters dynamically
        converted = [t(p) for t, p in zip(types, params)]

        # Special case for optional argument (list)
        if command == "list":
            if params:
                func(storage, params[0])
            else:
                func(storage)
        else:
            func(*converted, storage)

    except (ValueError, IndexError):
        print("Invalid arguments")
