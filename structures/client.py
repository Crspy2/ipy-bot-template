import asyncio
import atexit
from logging import Logger
import sys
import interactions as ipy
import asyncpg

from structures.config import Config

class AClient(ipy.Client):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs )
        self.config = Config
        self.logger: Logger = None
        self.db_conn: asyncpg.Connection = None

        self._loop = asyncio.get_event_loop()
        atexit.register(self._cleanup)
    
    def _cleanup(self):
        try:
            self.logger.info("Attempting to close DB connection")
            # self.db_cur.close()
            # self.db.close()
            self._loop.run_until_complete(self.db_conn.close())
            self.logger.info("Successfully closed DB connection")
        except Exception as err:
            self.logger.error(f"Failed to close DB connection for reason: {err}")

        self._loop.close()
        self.logger.info("Terminated Event Loop")

    def initialize_db(self, conn_str: str):
        try:
            self.db_conn = self._loop.run_until_complete(asyncpg.connect(conn_str))
            self.logger.info("Connected to DB")
        except Exception as err:
            self.logger.fatal(f"Error connecting to DB: {err}")
            sys.exit(1)