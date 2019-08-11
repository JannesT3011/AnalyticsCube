from discord.ext import commands
from core import Database
import pymongo

class BotJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print("drauf")
        try:
            Database().init_db(str(guild.id))
        except pymongo.errors.DublicateKeyError:
            return

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            Database().delete_db(str(guild.id))
        except Exception as err:
            print(err)
            return

def setup(bot):
    bot.add_cog(BotJoin(bot))