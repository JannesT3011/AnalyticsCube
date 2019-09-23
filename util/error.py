from discord.ext import commands
from discord import Embed

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """COMMAND HANDLER"""
        if isinstance(error, commands.CommandOnCooldown):
            """COOLDOWN ERROR"""
            embed = Embed(title="Calm down....", description=error)
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            """MISSING PERMISSIONS ERROR"""
            embed = Embed(title="Oops..", description="Sorry, but you don't have enough permissions to execute this command!")
            return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Error(bot))