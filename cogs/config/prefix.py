from discord.ext import commands
import discord
from dataminer import bot_requests
from CONFIG import DEFAULT_PREFIX

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def prefix(self, server_id: str):
        pr_list = self.bot.db.find({"_id": server_id})
        for pr in pr_list:
            prefix = pr["prefix"]

        return prefix, DEFAULT_PREFIX, f"<@{self.bot.user.id}>"

    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.command(name="prefix")
    async def _prefix(self, ctx):
        """SHOWS THE SERVER PREFIX """
        bot_requests(ctx.message, str(ctx.command), self.bot.db)

        embed = discord.Embed(title="Every prefix you can use on this server:", description=f", \n".join(self.prefix(str(ctx.guild.id))))
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Prefix(bot))