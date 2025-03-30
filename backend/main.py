import json
from dotenv import load_dotenv
import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

load_dotenv
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/humanized", methods=["POST"])
def humanize_text():
    data = request.json
    ai_text = data.get("aiText")

    if not ai_text:
        return jsonify({"error": "u gotta put in text bro"}), 400

    prompt = f"""
Here is what an AI detector looks for:
AI detectors are usually based on language models similar to those used in the AI writing tools they’re trying to detect. The language model essentially looks at the input and asks “Is this the sort of thing that I would have written?” If the answer is “yes,” it concludes that the text is probably AI-generated.

Specifically, the models look for two things in a text: perplexity and burstiness. The lower these two variables are, the more likely the text is to be AI-generated. But what do these unusual terms mean?

Perplexity
Perplexity is a measure of how unpredictable a text is: how likely it is to perplex (confuse) the average reader (i.e., make no sense or read unnaturally).

AI language models aim to produce texts with low perplexity, which are more likely to make sense and read smoothly but are also more predictable.
Human writing tends to have higher perplexity: more creative language choices, but also more typos.
Language models work by predicting what word would naturally come next in a sentence and inserting it. For example, in the sentence “I couldn’t get to sleep last …” there are more and less plausible continuations, as shown in the table below.

Levels of perplexity
Example continuation	Perplexity
I couldn’t get to sleep last night.	Low: Probably the most likely continuation
I couldn’t get to sleep last time I drank coffee in the evening.	Low to medium: Less likely, but it makes grammatical and logical sense
I couldn’t get to sleep last summer on many nights because of how hot it was at that time.	Medium: The sentence is coherent but quite unusually structured and long-winded
I couldn’t get to sleep last pleased to meet you.	High: Grammatically incorrect and illogical
Low perplexity is taken as evidence that a text is AI-generated.

Burstiness
Burstiness is a measure of variation in sentence structure and length—something like perplexity, but on the level of sentences rather than words:

A text with little variation in sentence structure and sentence length has low burstiness.
A text with greater variation has high burstiness.
AI text tends to be less “bursty” than human text. Because language models predict the most likely word to come next, they tend to produce sentences of average length (say, 10–20 words) and with conventional structures. This is why AI writing can sometimes seem monotonous.

Low burstiness indicates that a text is likely to be AI-generated.



    """

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    )

    output = jsonify(json.loads(completion.choices[0].message))
    return output


