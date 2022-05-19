from discord.ext import commands
from . import utcnow
import discord

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """SELECT DATA IF A USER UPDATES THEIR PROFILE"""
        roles = []
        for role in after.roles:
            roles.append(str(role))
        if before.nick != after.nick:
            push_data = {"timestamp": utcnow, "roles": roles}
            await self.bot.db.update_many({"_id": str(after.guild.id)}, {"$push": {"user_nickchange": push_data}})

        if isinstance(after.activities[0], discord.Spotify):
            push_data = {"timestamp": utcnow, "game": "spotify", "roles": roles}
            await self.bot.db.update_many({"_id": str(after.guild.id)}, {"$push": {"status": push_data}})

        if isinstance(after.activities[0], discord.Game):
            game = after.activities[0].name
            push_data = {"timestamp": utcnow, "game": game, "roles": roles}
            await self.bot.db.update_many({"_id": str(after.guild.id)}, {"$push": {"status": push_data}})
    
    #@commands.Cog.listener()
    #async def on_presence_update(self, before, after):
    #    """CALLED WHEN A MEMBER UPDATES THEIR STATUS/GAME"""
    #    print(before.status)
    #    print(after.status)

def setup(bot):
    bot.add_cog(Status(bot))