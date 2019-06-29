import discord
import creds

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("!meet"):
        message_list = message.content.split(' ')
        if len(message_list) < 4:
            err_msg = "{0.author.mention}: Incorrect usage: Not enough arguments. ".format(message)
            err_msg += "Correct usage: `!meet <meeting-subject> <mm-dd-yy> <hh-mm>`"
            await message.channel.send(err_msg)
        else:
            meeting_subject = message_list[1]
            meeting_date = message_list[2]
            meeting_time = message_list[3]
    
        # ToDo: Connect to Google calendar - get credentials and authenticate
        # ToDo: Create email list
        # ToDo: Send email list calendar invite 

@client.event
async def on_ready():
    print("Logged in as: ")
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    
client.run(creds.bot_token)