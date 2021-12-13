import os
import openai

openai.api_key = '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'
# openai.api_key = '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'

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

response = openai.Completion.create(
    engine="davinci",
    prompt=f"Q: How do I choose a laptop bag?\n{start_sequence}",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["\n"]
)
print(response.choices[0].text)