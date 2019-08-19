from discord.ext import commands
from Analytics import MessageAnalytics
from disputils import BotEmbedPaginator
from dataminer import bot_requests

class Analysis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @commands.group(name="analyze")
    async def _analyze(self, ctx):
        return

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_analyze.command(name="message")
    async def _analyze_message(self, ctx):
        msg = MessageAnalytics(str(ctx.guild.id)).analyze()
        paginator = BotEmbedPaginator(ctx, msg)
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        return await paginator.run()

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_analyze.command(name="reaction")
    async def _analyze_reaction(self, ctx):
        return

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_analyze.command(name="botrequests", aliases=["bot_requests", "bot-requests"])
    async def _analyze_botrequests(self, ctx):
        return

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_analyze.command(name="userjoins")
    async def _analyze_userjoins(self, ctx):
        return

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_analyze.command(name="userleaves")
    async def _analyze_userleaves(self, ctx):
        return

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_analyze.command(name="mentions")
    async def _analyze_mentions(self, ctx):
        return

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_analyze.command(name="botmsg", aliases=["bot_msg", "bot-msg"])
    async def _analyze_botmsg(self, ctx):
        return

def setup(bot):
    bot.add_cog(Analysis(bot))