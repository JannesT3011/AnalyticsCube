import discord
from discord.ext import commands
from . import utcnow

class Guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        push_data = {"timestamp": utcnow}
        await self.bot.db.update_many({"_id": str(invite.guild.id)}, {"$push": {"invite_create": push_data}})
    
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        push_data = {"timestamp": utcnow}
        await self.bot.db.update_many({"_id": str(after.guild.id)}, {"$push": {"guild_update": push_data}})


def setup(bot):
    bot.add_cog(Guild(bot))