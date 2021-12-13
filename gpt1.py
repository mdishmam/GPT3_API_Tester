import os
import openai

# Load your API key from an environment variable or secret management service
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'

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

prompt = 'Write a creative ad for the following product:\n""""""\n' + product_name + \
         '. ' + product_feats + '\n""""""\nEmphasize the word '+ emphasis +'\n""""""\n'

response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=200)
print(response.choices[0].text)