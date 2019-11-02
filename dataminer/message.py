from discord.ext import commands
from datetime import datetime
from . import utcnow
from . import bot_requests, bot_messages
from . import mentions_data
from CONFIG import DEFAULT_PREFIX

"""
COLLECT DATA FROM MESSAGES !
"""

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def prefix(self, server_id: str):
        pr_list = self.bot.db.find({"_id": server_id})
        for pr in pr_list:
            prefix = pr["prefix"]

        return (prefix, DEFAULT_PREFIX, f"<@{self.bot.user.id}>")

    @commands.Cog.listener()
    async def on_message(self, message):
        """EVENT IS CALLED WHEN A USER SENDS A MESSAGE"""
        # bot only respond to messages on a server!
        if not message.guild:
            return
        if message.author.bot:
            bot_messages(message, self.bot.db)
            return
        if len(message.role_mentions) > 0:
            mentions_data(message, self.bot.db)
            return
        if message.content.startswith(self.prefix(str(message.guild.id))):
            return
        # count messages here
        _roles = []
        for role in message.author.roles:
            _roles.append(str(role))
        push_data = {"msgid": str(message.id), "timestamp": utcnow, "roles": _roles, "channelid": str(message.channel.id)}
        # push the date into the database
        self.bot.db.update({"_id": str(message.guild.id)}, {"$push": {"message": push_data}})
        del _roles
        return

    @commands.command(name="test")
    async def _test(self, ctx):
        """ A test command!

        Testing stuff
        """
        bot_requests(ctx.message, str(ctx.command), self.bot.db)


def setup(bot):
    bot.add_cog(Message(bot))
