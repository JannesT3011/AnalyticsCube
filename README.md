# DiscordAnalytica
A discord bot that analyze your discord server 

# About
This bot fetches [data](https://github.com/Bmbus/DiscordAnalytica#Collected-Data) which will be safed in a MongoDb Database, you created!
Now you can see the data by using the [commands](https://github.com/Bmbus/DiscordAnalytica#commands-help). Data will be showed as plot or text-embed - debends on the command you use.
See examples [here](https://github.com/Bmbus/DiscordAnalytica#Examples)


# Collected Data

- `timestamp`-> what is used in which time
- `messageID`
- `serverID`
- `counts the userjoins/leaves`
- `counts messages`
- `status` -> which game was played the most
- `counts bot messages` -> bot requests
- `counts reactions` -> which reaction is used most
- `counts mentions`
NOTE: Private stuff such as passwords, mails or your ID won't collected!

# Commands (help)

Creates an embed in which the analyzed data of each category will shown
- `analyze message`
- `analyze reaction`
- `analyze botrequests`
- `analyze userjoins`
- `analyze userleaves`
- `analyze mentions`
- `analyze botmsg`

Creates a plot to each category 
- `plot message`
- `plot reaction`
- `plot botrequests`
- `plot userjoins`
- `plot userleaves`
- `plot mentions`
- `plot botmsg`


# Examples

For `analyze` commands:
![](https://github.com/Bmbus/DiscordAnalytica/tree/master/examples/example_embed.png)

For `plot` commands:
![](https://github.com/Bmbus/DiscordAnalytica/tree/master/examples/example_plot.png)
