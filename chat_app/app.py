from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ", 
        ["I can help you ",]
    ],
    [
        r"(.*) your name ?", 
        ["My name is nice's chatterbox, but you can just call me a chatbot.",]
    ],
    [
        r"how are you (.*)?|how are you ?", 
        ["I'm doing very well", "I am great!"]
    ],
    [
        r"sorry (.*)", 
        ["It's alright", "It's OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that"]
    ],
    [
        r"(hi|hey|hello|hola|holla|hy|hlo)(.*)",
        ["Hello! How can I assist you today?",]
    ],
    [
        r"what (.*) want ?", 
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*)created(.*)",
        ["Nice created me using Python's NLTK library ",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Ludhiana, India',]
    ],
    [
        r"(.*)raining in (.*)", 
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain",]
    ],
    [
        r"do you speak (.*)?",
        ["I primarily understand English, but I'm here to learn more!"]
    ],
    [
        r"what is (.*) (time|date)?",
        ["I'm not sure, but you can check your device for the current %1."]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"tell me about (.*)",
        ["What do you want to know about %1?"]
    ],
    [
        r"do you like (.*)?",
        ["I think %1 is interesting. What about you?"]
    ],
    [
        r"(.*)(sports|game|sport)(.*)", 
        ["I'm a very big fan of Cricket"]
    ],
    [
        r"quit",
        ["It was nice talking to you. See you soon :)"]
    ],
    [
        r"who is the prime minister of India?",
        ["Narinder Modi is the prime minister of India."]
    ],
    [
        r"(.*)",
        ["Sorry, I am not able to answer this."]
    ],
    [
        r"what's your favorite food?", 
        ["I don't eat, but I hear pizza is great!"]
    ],
    [
        r"do you have any hobbies?", 
        ["I enjoy chatting with people like you!"]
    ],    
    [
        r"what is artificial intelligence?", 
        ["Artificial intelligence (AI) is the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions."]
    ],
    [
        r"who is the father of ai?", 
        ["John McCarthy is considered the father of AI."]
    ],
    [
        r"what is machine learning?", 
        ["Machine learning is a subset of AI that focuses on building systems that learn from data and improve their performance over time without being explicitly programmed."]
    ],
    [
        r"what is deep learning?", 
        ["Deep learning is a subset of machine learning that uses neural networks with many layers (deep networks) to analyze various factors of data."]
    ],
    [
        r"what is a neural network?", 
        ["A neural network is a series of algorithms that attempt to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates."]
    ],
    [
        r"what is natural language processing?", 
        ["Natural language processing (NLP) is a branch of AI that helps computers understand, interpret, and respond to human language."]
    ],
    [
        r"what is flask",
        ["Flask is a lightweight WSGI web application framework in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications."]
    ],
    [
        r"how do you implement machine learning in NLP",
        ["Machine learning in NLP can be implemented using various techniques like supervised learning, unsupervised learning, and reinforcement learning to create models that understand and generate human language."]
    ],
    [
        r"what are common NLP tasks",
        ["Common NLP tasks include sentiment analysis, machine translation, named entity recognition, and speech recognition."]
    ],
    [
        r"what is tokenization in NLP",
        ["Tokenization is the process of breaking down text into smaller units called tokens. These tokens could be words, characters, or subwords."]
    ],
    [
        r"what is an LSTM network",
        ["Long Short-Term Memory (LSTM) networks are a type of recurrent neural network capable of learning long-term dependencies. They are well-suited to classifying, processing, and making predictions based on time series data."]
    ],
    [
        r"what is NLTK",
        ["The Natural Language Toolkit (NLTK) is a Python library for working with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources."]
    ],
] 

chat = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    response = chat.respond(user_text)
    return render_template("index.html", user_text=user_text, bot_response=response)

if __name__ == "__main__":
    app.run(debug=True)