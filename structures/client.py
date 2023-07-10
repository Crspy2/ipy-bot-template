import asyncio
import atexit
from logging import Logger
import sys
import interactions as ipy

from structures.config import Config

class AClient(ipy.Client):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs )
        self.config = Config
        self.logger: Logger = None

        atexit.register(self._cleanup)
    
    def _cleanup(self):
        # Code to run when bot closes
        self.logger.info("Bot Cleanup Finished")
