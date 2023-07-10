import os
from structures.client import AClient


def load_events(client: AClient):
    handlers_dir = os.path.dirname(os.path.abspath(__file__))
    events_dir = os.path.join(os.path.dirname(handlers_dir), 'events')

    events = []
    for root, dirs, files in os.walk(events_dir):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for module in files:
            if module not in ("__init__.py", "template.py") and module[-3:] == ".py":
                module_path = os.path.join(root, module)
                module_name = module_path[len(os.path.dirname(events_dir)) + 1:-3].replace(os.sep, ".")
                events.append(module_name)

    for event in events:
        try:
            client.load_extension(event)
            client.logger.info(f"Loaded the {event[7:].title().replace('.', '-')} event")
        except Exception as err:
            client.logger.error(f"Failed to load the  {event[7:].title().replace('.', '-')} event!\n{err}")