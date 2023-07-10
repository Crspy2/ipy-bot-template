import os
from structures.client import AClient


def load_commands(client: AClient) -> None:
    handlers_dir = os.path.dirname(os.path.abspath(__file__))
    commands_dir = os.path.join(os.path.dirname(handlers_dir), 'commands')
    commands = []
    for root, dirs, files in os.walk(commands_dir):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for module in files:
            if module not in ("__init__.py", "template.py") and module[-3:] == ".py":
                module_path = os.path.join(root, module)
                module_name = module_path[len(os.path.dirname(commands_dir)) + 1:-3].replace(os.sep, ".")
                commands.append(module_name)

    for cmd in commands:
        try:
            client.load_extension(cmd)
            client.logger.info(f"Loaded the {cmd[5:].title().replace('.', '-')} command")
        except Exception as err:
            client.logger.error(f"Failed to load the  {cmd[5:].title().replace('.', '-')} command!\n{err}")
