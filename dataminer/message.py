import discord
from discord.ext import commands
from . import utcnow

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """EVENT IS CALLED WHEN A USER SEND A MESSAGE"""
        if not message.guild:
            return
        if message.author.bot:
            # TODO count bot messages
            return
        if len(message.role_mentions) > 0:
            # TODO count mentions in message
            return
        if message.content.startswith("da."):
            return
        
        roles = [role for role in message.author.roles]

        push_data = {"msgid": str(message.id), "timestamp": utcnow, "roles": roles, "channelid": str(message.channel.id)}
        # TODO add to db
        return

def setup(bot):
    bot.add_cog(Message(bot))