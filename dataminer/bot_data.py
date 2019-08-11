import discord
from . import utcnow


def bot_requests(message: discord.message.Message, cmd_name:str, db):
    """SELECT DATA IF A COMMAND IS CALLED (ONLY THIS BOT)"""
    _roles = []
    for role in message.author.roles:
        _roles.append(str(role))
    push_data = {"cmdname": cmd_name, "timestamp": utcnow, "channelid": str(message.channel.id), "roles": _roles}
    print(push_data)
    db.update({"_id": str(message.guild.id)}, {"$push": {"bot_requests": push_data}})
    del _roles
    return


def bot_messages(message: discord.message.Message, db):
    """SELECT DATA FROM BOT MESSAGES"""
    _roles = []
    for role in message.author.roles:
        _roles.append(str(role))
    push_data = {"msgid": str(message.id), "timestamp": utcnow, "roles": _roles, "channelid": str(message.channel.id)}
    db.update({"_id": str(message.guild.id)}, {"$push": {"bot_msg": push_data}})
    del _roles
    return