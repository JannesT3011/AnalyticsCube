from discord.ext import commands
from dataminer.bot_data import bot_requests
from discord import Embed
from datetime import datetime


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.command(name="stats")
    async def _stats(self, ctx):
        """Get general stats of the server

        This command can only be used on a server
        """
        await bot_requests(ctx.message, str(ctx.command), self.bot.db)
        data = await self.bot.db.find_one({"_id": str(ctx.guild.id)})

        embed = Embed(title=f"{ctx.guild.name} ~ general stats", timestamp=datetime.utcnow())
        embed.add_field(name="Total messages send:*", value=f"{len(data['message'])}", inline=True)
        embed.add_field(name="Total message edited:*", value=f"{len(data['message_edit'])}", inline=True)
        embed.add_field(name="Total message deleted:*", value=f"{len(data['message_delete'])}", inline=True)
        embed.add_field(name="Total reactions added:*", value=f"{len(data['reaction'])}", inline=True)
        embed.add_field(name="Total bot requests:*", value=f"{len(data['bot_requests'])}", inline=True)
        embed.add_field(name="Total bot messages:*", value=f"{len(data['bot_msg'])}", inline=True)
        embed.add_field(name="Total user-joins:*", value=f"{len(data['userjoins'])}", inline=True)
        embed.add_field(name="Total user-leaves:*", value=f"{len(data['userleave'])}", inline=True)
        embed.add_field(name="Total mentions:*", value=f"{len(data['mentions'])}", inline=True)
        embed.add_field(name="Total status/game changes counted:*", value=f"{len(data['status'])}")
        embed.add_field(name="Total user bans counted:*", value=len(data['user_ban']), inline=True)
        embed.add_field(name="Total user bans counted:*", value=len(data['user_unban']), inline=True)
        embed.add_field(name="Total voice joins/leaves:*", value=len(data['voice']), inline=True)
        embed.add_field(name="Total nickname changes counted:*", value=len(data['user_nickchange']), inline=True)
        embed.add_field(name="Total invites created:", value=len(data['invite_create']), inline=True)
        embed.add_field(name="Total guild updated counted:*", value=len(data['guild_update']), inline=True)
        embed.add_field(name="Total users:", value=f"{ctx.guild.member_count}", inline=True)
        embed.add_field(name="Total text channels:", value=len(ctx.guild.text_channels), inline=True)
        embed.add_field(name="Total voice channels", value=len(ctx.guild.voice_channels), inline=True)
        embed.set_footer(text=f"Since I joined the server: {data['server_join']}", icon_url=self.bot.user.avatar_url) # TODO add total users, channels ...

        return await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Stats(bot))