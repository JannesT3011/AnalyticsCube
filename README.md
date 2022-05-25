# AnalyticsCube
This bot collects data of your discord server and make it accessible for you!

<img src="https://github.com/JannesT3011/DiscordAnalytica/blob/rewrite/botlogo.png" alt="EXAMPLE-PLOT"> 

### Run it by yourself

Clone the repo and redirect into it: 
```bash
git clone https://github.com/JannesT3011/AnalyticsCube/tree/master
cd AnalyticsCube/
```
Install all requirements:
```bash
pip3 install -r requirements.txt
```

Create `config.py` file:
```bash
nano config.py
```

This file should look like this:
```python
# DISCORD BOT CONFIG
TOKEN = ""
PREFIX = ""

# DATABASE CONFIG
CONNECTION = ""
CLUSTER = ""
DB = ""

#IMGUR API CONFIG
IMGUR_CLIENT_ID = ""
IMGUR_CLIENT_SECRET = ""
```
Fill in your credentials and data

Start the bot:
```bash
python3 bot.py
```

### Commands
 | Name | Info |
| --- | ----------- |
| stats | Stats about the server data (size, etc) |
| analyze `category`*| Give you stats about the collected data and category |
| plot `category`*| Plot collected data of given category|
| blacklist `add/remove`| Blacklist channel! (In this channel will be no data collected) |
| userinfo `user`| Infos about a given user |
| roleinfo `role`| Infos about a given role |

! All commands can only be executed from users with admin rights !


`* see categorys in fallowing table` 

### Which data will be collected?

 | Category/Name | Data that will be collected |
| --- | ----------- |
| `message` | `timestamp`, `roles of author`, `channelid`, `attachments`
| `message_edit` | `timestamp`, `roles of author`, `channelid`
| `message_delete` | `timestamp`, `roles of author`, `channelid`
 | `mentions` | `timestamp`, `role (of author) that was mentioned`, `roles of author`, `channelid`
 | `botrequests` | `timestamp`, `command name`, `channelid`, `role of author`
 | `botmsg` | `timestamp`, `roles of author`, `channelid`
 | `reactions` | `timestamp`, `name of reaction`, `role of author`, `channelid`
 | `userjoin` | `timestamp`
 | `userleaves` | `timestamp`
 | `user_ban` | `timestamp`
 | `user_unban` | `timestamp` 
 | `user_nickchange` | `timestamp`, `role of author`
 | `game/status` | `timestamp`, `game`, `role of user`
 | `voice` | `timestamp`, `join/leave`, `role of user`, `channelid`, `afk status`, `stream`, `video status (on/off)`
 | `invites` | `timestamp`
 | `guild_updates` | `timestamp`
 | `users` | `timestamp`, `user count`

### Whats will be NOT collected?

- `user information` such as your id, mail ...
- `Spotify track` the name of the song you listen to
- `message ids`

You can also blacklist channels, so that no data will collected in these!

### TODOs
- [ ] new logo (first row one cube, sec two cubes, third three cubes)
- [X] async pymongo
- [X] message delete
- [X] message edit
- [X] message attechment (files etc.)
- [X] on_member_update select more data, like nikname change...
- [X] on_guild_update
- [X] kick, ban, unban
- [X] invite create
- [X] voice channel 
- [X] count users
- [X] how much messages did this bot send?
- [X] role info
- [X] user info
- [ ] config command
- [X] blacklist channel
- [X] plot > imgur api
- [ ] user plot
- [ ] blacklist specific data that then not will be collected
- [ ] interfaces -> when send cs.plot/analyze without argument SELECT option of category