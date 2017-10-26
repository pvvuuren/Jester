import discord
import asyncio
import random
from messages import messages_list
from copy import deepcopy

client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="with my thingie"))
    messages = deepcopy(messages_list)
    cleanmessages = deepcopy(messages_list)
    while not client.is_closed:
        channel = client.get_channel("360701697963851776")
        if not messages:
            messages = deepcopy(cleanmessages)
        await client.send_message(channel, messages.pop(random.randrange(0, len(messages))))
        await asyncio.sleep(90)

client.loop.create_task(background_loop())
client.run("MzYwNjg1NTM0NTk2ODI1MDkx.DKuSoQ.Prdbtg0W66L_WztPOqO-nDOgzWE")



