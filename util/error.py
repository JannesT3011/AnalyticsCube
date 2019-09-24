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
        elif isinstance(error, commands.BotMissingPermissions):
            owner = ctx.guild.owner_id
            embed = Embed(title="Oops..", description="Sorry, but I can't send messages on your server, because I don't have enough permissions!")
            return await owner.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            embed = Embed(title="Oops..", description=f"This command doesnt exist! Try `{self.bot.command_prefix}help` to see all commands")
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.CheckFailure):
            embed = Embed(title="Oops...", description="It seems like you arn't allowed to execute this command.,")
            return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Error(bot))