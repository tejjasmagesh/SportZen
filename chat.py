import nltk
from nltk.chat.util import Chat, reflections
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Sports-Zen. You can call me BEE!",]
    ],
    [
        r"I would like to book an arena ?",
        ["which arena would you like to book?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Do you need anything else?:)",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Someone created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bangalore, Karnataka',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2"]
    ],
    ]
def chat():
    '''print("Hi! I am a chatbot created by Sports-Zen for your service")
    chat = Chat(pairs, reflections)
    chat.converse()'''
    
    print("Hi! I am a chatbot created by Analytics Vidhya for your service")
    chat = Chat(pairs, reflections)
    while True:
        msg = input("msg:")
        print(chat.respond(msg))
        if msg in 'byeGoodbye':
            print(chat.respond(msg))
            break
#initiate the conversation
if __name__ == "__main__":
    chat()   
 
