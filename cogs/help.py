import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='help', invoke_without_command=True)
    async def help(self, ctx):
        return await ctx.send('test')
    
    @help.command(name="analyze")
    async def help_analyze(self, ctx):
        return
    
    @help.command(name="plot")
    async def help_plot(self, ctx):
        return

async def setup(bot):
    await bot.add_cog(Help(bot))