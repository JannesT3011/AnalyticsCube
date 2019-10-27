from discord.ext import commands
from . import utcnow
import discord

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """SELECT DATA IF A USER START PLAYING A GAME"""
        try:
            game_type = after.activities[0]
            if isinstance(game_type, discord.Spotify) or isinstance(game_type, discord.Game):
                _roles = []
                for role in after.roles:
                    _roles.append(str(role))

                game = after.activities[0].name
                push_data = {"game": game, "timestamp": utcnow, "roles": _roles}
                self.bot.db.update({"_id": str(after.guild.id)}, {"$push": {"status": push_data}})
                del _roles
                return

            return
        except IndexError:
            pass


def setup(bot):
    bot.add_cog(Status(bot))