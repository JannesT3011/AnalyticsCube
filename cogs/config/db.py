from discord.ext import commands
from . import is_bot_owner
from dataminer import bot_requests

class Db_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @is_bot_owner()
    @commands.group(name="db")
    async def _db(self, ctx):
        return

    @is_bot_owner()
    @commands.cooldown(1, 20.0, commands.BucketType.user)
    @_db.command(name="add_field", aliases=["addfield", "fieldadd", "field_add"])
    async def _db_addfield(self, ctx, *, field_name: str, type):
        """CREATE A NEW FIELD IN THE DATABASE"""
        bot_requests(ctx.message, str(ctx.command), self.bot.db)

        types = {
            "list": [],
            "object": {},
            "string": "",
            "int": int
        }
        self.bot.db.update_one({"_id": str(ctx.guild.id)}, {"$set": {field_name: types[type]}})


def setup(bot):
    bot.add_cog(Db_cmds(bot))