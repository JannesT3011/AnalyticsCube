import discord
from discord.ext import commands

class Role_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.command(name='role', aliases=["roleinfo"])
    async def name_command(self, ctx, *, role:discord.Role):
        
        embed = discord.Embed(title=f"Infos for {role.name}", color=role.color)
        embed.add_field(name="Total users with this role", value=len(role.members), inline=False)
        #embed.add_field(name="Permissions", value=role.permissions, inline=False)
        embed.add_field(name="Premium role", value="Yes" if role.is_premium_subscriber() else "No", inline=False)
        embed.add_field(name="Created at:", value=str(role.created_at).split(".")[0])

        return await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Role_info(bot))