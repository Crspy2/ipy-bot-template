from interactions import listen, Extension

from structures.client import AClient

class OnReady(Extension):
    def __init__(self, client: AClient):
        self.client: AClient = client

    @listen()
    async def on_ready(self):
        self.client.logger.start(f"Logged in as {self.bot.user.display_name} (ID: {self.bot.user.id})")


def setup(client: AClient):
    OnReady(client)