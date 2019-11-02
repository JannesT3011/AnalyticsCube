from discord.ext import commands
from . import is_bot_owner
import discord
import asyncio

class Set(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.cooldown(1, 7.0, commands.BucketType.user)
    @commands.group(name="set")
    async def _set(self, ctx):
        """RETURN ALL AVAILABLE SET FUNCTIONS"""
        return

    @is_bot_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_set.command(name="game")
    async def _set_game(self, ctx, *, game_name: str):
        """SET BOT GAME"""
        await self.bot.change_presence(game=discord.Game(name=game_name))
        await ctx.send(f"Game changed to: `{game_name}`")

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_set.command(name="prefix")
    async def _set_prefix(self, ctx, *, prefix: str):
        """SET A SERVER PREFIX"""
        self.bot.db.update({"_id": str(ctx.guild.id)}, {"$set": {"prefix": prefix}})

        await ctx.send("React with 👌 to change the prefix!")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "👌"

        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("Seems like you don't want to change the prefix, try again later!")
        else:
            embed = discord.Embed(title=f"Server-prefix changed to: `{prefix}`!")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Set(bot))