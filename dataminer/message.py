import discord
from discord.ext import commands
from . import utcnow
from .bot_data import bot_messages, bot_requests
from .mentions import mentions_data
from config import PREFIX

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """EVENT IS CALLED WHEN A USER SEND A MESSAGE"""
        if not message.guild:
            return
        if message.author.bot:
            await bot_messages(message, self.bot.db)
            return
        if len(message.role_mentions) > 0:
            await mentions_data(message, self.bot.db)
            return
        if message.content.startswith(PREFIX):
            return
        roles = []
        for role in message.author.roles:
            roles.append(str(role))

        push_data = {"timestamp": utcnow, "roles": roles, "channelid": str(message.channel.id), "attachments": True if len(message.attachments) > 0 else False}
        await self.bot.db.update_many({"_id": str(message.guild.id)}, {"$push": {"message": push_data}})
        return
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        roles = []
        for role in after.author.roles:
            roles.append(str(role))
        push_data = {"timestamp": utcnow, "roles": roles, "channelid": after.channel.id}
        await self.bot.db.update_many({"_id": str(after.guild.id)}, {"$push": {"message_edit": push_data}})
        return
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        roles = []
        for role in message.author.roles:
            roles.append(str(role))
        push_data = {"timestamp": utcnow, "roles": roles, "channelid": message.channel.id}
        await self.bot.db.update_many({"_id": str(message.guild.id)}, {"$push": {"message_delete": push_data}})
        return


def setup(bot):
    bot.add_cog(Message(bot))