import discord
from . import utcnow

def mentions_data(message: discord.message.Message, db):
    """COLLECT DATA IF A ROLE IS MENTIONED"""
    _roles = []
    _ment_role = []

    for role in message.author.roles:
        _roles.append(str(role))

    for mrole in message.role_mentions:
        _ment_role.append(str(mrole))

    push_data = {"ment_role": _ment_role, "timestamp": utcnow, "roles": _roles, "channelid": str(message.channel.id)}
    db.update({"_id": str(message.guild.id)}, {"$push": {"mentions": push_data}})

    del _roles
    del _ment_role