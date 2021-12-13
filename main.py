import json

import requests


gptKey = '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'
product_name = 'Samsung Electronics SM-N986UZNAXAA'
product_feats = 'S PEN & SAMSUNG NOTES: Pen precision meets PC power with S Pen & Samsung Notes.\
INTELLIGENT BATTERY & SUPER FAST CHARGE: All-day intelligent battery learns how to optimize battery life, while super fast charging boosts your battery in minutes¹.\
DISPLAY & GAMING: Breathtaking screen refresh rate, adaptive Dynamic AMOLED 2X display, Galaxy 5G support & advanced processor, allows for a smooth gaming experience.Bluetooth:5.0, A2DP, LE, aptX\
HYPERFAST PROCESSOR: Samsung’s fastest Note processor transforms your gaming and binging with less interruption.\
POINT-TO-SHARE: Share information directly with other compatible Samsung devices.\
EXPANDABLE MEMORY: Store all your photos and videos with up to 1TB of expandable memory with MicroSD card (sold separately).\
POWER OF 5G: Get next-level power for everything you love to do with Samsung Galaxy 5G: share more, game harder, experience more.\
¹Battery power consumption depends on usage patterns and results may vary.'
emphasis = 'A good phone'

prompt = 'Write a creative ad for the following product:\n""""""\n' + product_name +\
         '. ' + product_feats + '\n""""""\nEmphasize the word '+ emphasis +'\n""""""\n'

data = {
    "prompt": prompt,
    "temperature": 1,
    "max_tokens": 200,
    "top_p": 0.8,
    "frequency_penalty": 0.8,
    "presence_penalty": 0.0,
    "stop": '""""""'
}
url = 'https://api.openai.com/v1/engines/davinci-instruct-beta/completions'
headers = {'Authorization': 'Bearer '+gptKey, 'Content-Type': 'application/json'}
dataJson = json.dumps(data)
# response = requests.post(url, data={key: value}, json={key: value}, args)
response = requests.post(url, headers=headers, data=dataJson)

