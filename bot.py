import asyncio

import discord
import os

import image_generator

prefix = '~osu '


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.loop.create_task(self.update_guild_count())

    async def update_guild_count(self):
        while True:
            guild_count = len(self.guilds)
            await self.change_presence(activity=discord.Game(name="on {} servers".format(guild_count)))
            await asyncio.sleep(300)

    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            return

        # Command handler
        if message.content.startswith(prefix):
            text = message.content.replace(prefix, '')
            image_path = await image_generator.generate_osu_image(text, message.author.id)
            await message.channel.send(file=discord.File(image_path))
            os.remove(image_path)


def get_token_from_file():

    with open('token', 'r+') as token_file:
        return token_file.read()


def start():
    token = get_token_from_file()
    client = MyClient()
    client.run(token)


if __name__ == '__main__':
    start()
