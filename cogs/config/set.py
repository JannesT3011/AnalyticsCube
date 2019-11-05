from discord.ext import commands
from . import is_bot_owner
import discord
import asyncio
from dataminer import bot_requests

class Set(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.cooldown(1, 7.0, commands.BucketType.user)
    @commands.group(name="set")
    async def _set(self, ctx):
        """RETURN ALL AVAILABLE SET FUNCTIONS"""
        bot_requests(ctx.message, str(ctx.command), self.bot.db)

        embed = discord.Embed(title="`Set` commands")
        embed.add_field(name="`set game <NAME>`", value="Set the game/status of the bot", inline=False)
        embed.add_field(name="`set prefix <PREFIX>`", value="Set the server prefix", inline=False)
        return await ctx.send(embed=embed)

    @is_bot_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_set.command(name="game")
    async def _set_game(self, ctx, *, game_name: str):
        """SET BOT GAME"""
        bot_requests(ctx.message, str(ctx.command), self.bot.db)

        await ctx.send(f"React with 👌 to change the game to `{game_name}`!")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "👌"

        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("Sees like you don't want to change the prefix, try again later!")
        else:
            await self.bot.change_presence(activity=discord.Game(name=game_name))
            embed = discord.Embed(title=f"Bot-game changed to: `{game_name}`!")
            return await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.cooldown(1, 10.0, commands.BucketType.user)
    @_set.command(name="prefix")
    async def _set_prefix(self, ctx, *, prefix: str):
        """SET A SERVER PREFIX"""
        bot_requests(ctx.message, str(ctx.command), self.bot.db)

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
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Set(bot))