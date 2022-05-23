from click import command
import discord
from discord.ext import commands
from . import utcnow

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        roles = []
        for role in member.roles:
            roles.append(str(role))

        if before.channel is None:
            push_data = {"join": True, "timestamp": utcnow, "roles": roles,"channel": after.channel.id, "afk": after.afk, "stream": after.self_stream, "video": after.self_video}
            await self.bot.db.update_many({"_id": str(member.guild.id)}, {"$push": {"voice": push_data}})
        if after.channel is None:
            push_data = {"join": False, "timestamp": utcnow, "roles": roles, "channel": before.channel.id, "afk": after.afk, "stream": after.self_stream, "video": after.self_video}
            await self.bot.db.update_many({"_id": str(member.guild.id)}, {"$push": {"voice": push_data}})

def setup(bot):
    bot.add_cog(Voice(bot))