from discord.ext import commands
from discord import Embed


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def _help(self, ctx):
        cat = ["`message`", "`reaction`", "`bot-requests`", "`userjoins`", "`userlaves`", "`mentions`", "`bot-msg`"]
        embed = Embed(title=f"{self.bot.user.name} ~ Help")
        embed.add_field(name="`stats`", value="Shows general stats", inline=False),
        embed.add_field(name="`analyze`", value="Analyze a specific category", inline=False)
        embed.add_field(name="`analyze` ~ categories", value="\n".join(cat))

        return await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))