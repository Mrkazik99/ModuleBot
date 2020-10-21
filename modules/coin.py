import random

EN = ['heads', 'tails']


async def coin_flip():
    return {'Flip a coin': '{"desc": "", "text": "' + EN[random.randint(0, 1)] + '", "withImage": "False"}'}
