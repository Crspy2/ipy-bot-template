import time
from interactions import EmbedField, Extension, slash_command, SlashContext, Embed

from structures.client import AClient

class PingCmd(Extension):
    def __init__(self, client) -> None:
        self.client: AClient = client
    
    @slash_command()
    async def ping(self, ctx: SlashContext):
        start_time = time.time()
        msg = await ctx.send("Pinging!")
        end_time = time.time()
        self.bot.logger.say(self.bot.latency)
        self.bot.logger.say(self.bot.ws.latency)
        await msg.edit(embed=Embed(
            title="Pong!",
            color=self.client.config.colors.green,
            fields=[
                EmbedField("Client Ping:", f"{(end_time-start_time):.2f}", True),
                EmbedField("Websocket Ping", f"{self.client.ws.latency:.2f}", True)
                ]
        ))

def setup(client: AClient):
    PingCmd(client)