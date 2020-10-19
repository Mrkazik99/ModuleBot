import logging
import yaml
from telethon import TelegramClient, events
from moduleslist import functions_list as commands
from moduleslist import create_answer
from telethon.tl.types import InputWebDocument
import json

with open("login.yml", 'r') as f:
    config = yaml.safe_load(f)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

client = TelegramClient(**config['telethon_settings']).start(bot_token=config['bot_token'])


@client.on(events.InlineQuery)
async def inline_query(event):
    builder = event.builder
    ans = []
    if not event.text or len(event.text) < 3:
        for entry, value in commands.items():
            value_json = json.loads(value)
            ans.append(await builder.article(entry, text=value_json['text'], description=value_json['desc']))
        await event.answer(ans)
        return
    else:
        ans_list = await create_answer(event.text)
        for entry, value in ans_list.items():
            value_json = json.loads(value)
            if value_json['withImage'] == 'True':
                ans.append(await builder.article(entry, text=value_json['text'], description=value_json['desc'],
                                                 thumb=InputWebDocument(url=value_json['imageUrl'], size=0,
                                                                        mime_type=value_json['imageType'],
                                                                        attributes=[], )))
            else:
                ans.append(await builder.article(entry, text=value_json['text'], description=value_json['desc']))
        await event.answer(ans)
        return


@client.on(events.NewMessage)
async def answer(event):
    if event.text == '/start':
        await event.reply('Siema mały kurwiu 😂')
    if event.text.startswith('@'):
        await event.respond('It\'s me 😂')


with client:
    print('Good morning!')
    client.run_until_disconnected()
