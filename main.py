import os
import sys
import interactions as ipy

from dotenv import load_dotenv
from handlers.commandHandler import load_commands
from handlers.eventHandler import load_events

import logutil
from structures.client import AClient

load_dotenv()

logger = logutil.init_logger("Altera")

if not os.environ.get("DISCORD_TOKEN"):
    logger.critical("TOKEN variable not set. Cannot continue")
    sys.exit(1)

client = AClient(
    token=os.environ.get("DISCORD_TOKEN"),
    intents=ipy.Intents.DEFAULT | ipy.Intents.GUILD_MEMBERS,
    debug_scope=os.environ.get("DEBUG_SCOPE"),
    owner_ids=[385568884511473664],
    logger=logger,

    # Optional
    disable_dm_commands=True,
    show_ratelimit_tracebacks=True,
)

client.logger = logger

load_events(client)
load_commands(client)

client.start()

