from discord.ext import commands
from datetime import datetime
from . import utcnow
import unicodedata
from util.checks import in_blacklist

"""
COLLECT DATA FROM REACTIONS !
"""

class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """EVENT IS CALLED WHEN A USER ADDS AN REACTION"""
        if in_blacklist(self.bot.db, reaction.message.guild, reaction.message.channel):
            return
        if not reaction.message.guild:
            return
        if user.bot:
            return
        _roles = []
        for role in user.roles:
            _roles.append(str(role))
        emote = unicodedata.name(reaction.emoji[0])
        push_data = {"reactionname": str(emote.lower()), "timestamp": utcnow, "roles": _roles, "channelid": str(reaction.message.channel.id)}
        # push the date into the database
        await self.bot.db.update_many({"_id": str(reaction.message.guild.id)}, {"$push": {"reaction": push_data}})
        return

def setup(bot):
    bot.add_cog(Reaction(bot))