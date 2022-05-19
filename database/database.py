import motor.motor_asyncio as motor
from datetime import datetime
from dataminer import utcnow
from config import CONNECTION, CLUSTER, DB  

class DbClient:
    """CREATES A CONNECTION TO YOUR DATABASE"""
    def __init__(self):
        cluster = motor.AsyncIOMotorClient(CONNECTION)
        db = cluster[CLUSTER]
        self.collection = db[DB]

    def __call__(self, *args, **kwargs):
        return self.collection


class Database(DbClient):
    """EXECUTE DATABASE STUFF"""
    async def init_db(self, userid: str):
        try:
            await self.collection.insert_one(db_layout(userid))
            return
        except:
            raise

    async def delete_db(self, userid: str):
        try:
            await self.collection.delete_one({"_id": userid})
            return
        except:
            raise

def db_layout(guildid: str):
    """DEFAULT DATABASE LAYOUT"""
    default_data = {"_id": guildid,
                    "message": [],
                    "message_delete": [],
                    "message_edit": [],
                    "reaction": [],
                    "bot_msg": [],
                    "bot_requests": [],
                    "users": [],
                    "userjoins": [],
                    "userleave": [],
                    "mentions": [],
                    "user_ban": [],
                    "user_unban": [],
                    "voice": [],
                    "user_nickchange": [],
                    "status": [],
                    "invite_create": [],
                    "other_prefix": [],
                    "guild_update": [],
                    "prefix": "",
                    "server_join": utcnow,
                    }

    return default_data