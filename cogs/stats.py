from discord.ext import commands
from dataminer import bot_requests
from discord import Embed
from datetime import datetime


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.command(name="stats")
    async def _stats(self, ctx):
        """Get general stats of the server

        This command can only be used on a server
        """
        bot_requests(ctx.message, str(ctx.command), self.bot.db)
        data = self.bot.db.find_one({"_id": str(ctx.guild.id)})

        embed = Embed(title=f"{ctx.guild.name} ~ general stats", timestamp=datetime.utcnow())
        embed.add_field(name="Total messages send:*", value=f"{len(data['message'])}", inline=False)
        embed.add_field(name="Total reactions added:*", value=f"{len(data['reaction'])}", inline=False)
        embed.add_field(name="Total bot requests:*", value=f"{len(data['bot_requests'])}", inline=False)
        embed.add_field(name="Total user-joins:*", value=f"{len(data['userjoins'])}", inline=False)
        embed.add_field(name="Total user-leaves:*", value=f"{len(data['userleave'])}", inline=False)
        embed.add_field(name="Total mentions:*", value=f"{len(data['mentions'])}", inline=False)
        embed.add_field(name="Total bot messages:*", value=f"{len(data['bot_msg'])}", inline=False)
        embed.set_footer(text=f"Since I joined the server: {data['server_join']}", icon_url=self.bot.user.avatar_url)

        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Stats(bot))