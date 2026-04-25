import sys
from task_cli.dispatcher import dispatch
from task_cli.storage import Storage

def main():
    storage = Storage("tasks.json")
    args = sys.argv[1:]

    if not args:
        print("No command provided")
        return

    dispatch(args, storage)


if __name__ == "__main__":
    main()