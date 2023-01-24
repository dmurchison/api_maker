from app.config import Config

class DatabaseClient:
    def __init__(self, config: Config):
        self.config = config
        self.client = None

    async def connect(self):
        self.client = await self.config.db.connect()

    async def disconnect(self):
        await self.client.disconnect

