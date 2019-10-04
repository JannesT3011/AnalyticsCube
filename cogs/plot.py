from Analytics.graphics import create_plot
from discord.ext import commands
import discord
from dataminer import bot_requests

class Plot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @commands.group(name="plot")
    async def _plot(self, ctx):
        return

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_plot.command(name="message")
    async def _plot_message(self, ctx):
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        create_plot("message", str(ctx.guild.id))
        img = discord.File(f"./src/img/{str(ctx.guild.id)}_message.png")
        return await ctx.send(file=img)

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_plot.command(name="reaction")
    async def _plot_reaction(self, ctx):
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        create_plot("reaction", str(ctx.guild.id))
        img = discord.File(f"./src/img/{str(ctx.guild.id)}_reaction.png")
        return await ctx.send(file=img)

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_plot.command(name="botrequest", aliases=["bot_request", "bot-requests"])
    async def _plot_botrequests(self, ctx):
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        create_plot("bot_requests",str(ctx.guild.id))
        img = discord.File(f"./src/img/{str(ctx.guild.id)}_bot_requests.png")
        return await ctx.send(file=img)

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_plot.command(name="userjoins", aliases=["userjoin"])
    async def _plot_userjoins(self, ctx):
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        create_plot("userjoin", str(ctx.guild.id))
        img = discord.File(f"./src/img/{str(ctx.guild.id)}_userjoins.png")
        return await ctx.send(file=img)

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_plot.command(name="userleaves", aliases=["userleave"])
    async def _plot_userleaves(self, ctx):
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        create_plot("userleave", str(ctx.guild.id))
        img = discord.File(f"./src/img/{str(ctx.guild.id)}_userleave.png")
        return await ctx.send(file=img)

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_plot.command(name="mentions", aliases=["mention"])
    async def _plot_mentions(self, ctx):
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        create_plot("mentions", str(ctx.guild.id))
        img = discord.File(f"./src/img/{str(ctx.guild.id)}_mentions.png")
        return await ctx.send(file=img)

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_plot.command(name="botmsg", aliases=["bot_msg", "bot-msg"])
    async def _plot_botmsg(self, ctx):
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        create_plot("bot_msg", str(ctx.guild.id))
        img = discord.File(f"./src/img/{str(ctx.guild.id)}_bot_msg.png")
        return await ctx.send(file=img)

def setup(bot):
    bot.add_cog(Plot(bot))