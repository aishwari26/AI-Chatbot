#import useful libraries
import random
#define some sample responses
greeting =['Hey There! How can i help you today?',
'Hello! How can i help you today?',
'hi there! what can i do for you today?',
'Hello there! Need any assistance?'
]

help_response=[
    'I can help you with general questions. just ask!',
    'I can tell you some fun facts',
    'I can tell you some jokes'
]

jokes=[ 'I used to play piano by ear, but now I use my hands',
       'Parallel lines have so much in common, it’s a shame they’ll never meet',
       'I have a few jokes about unemployed people, but none of them work',
       'I told my doctor that I broke my arm in two places, and he told me to stop going to those places'
       ]

facts=[ 'Bananas are technically classified as berries, but strawberries are not.',
       'Octopuses have three hearts, nine brains, and blue blood.',
       'Wombat poop is cube-shaped, which stops it from rolling away.'
]




#FUNCTIONS



## response function

def chatty_response(user_input):
    '''This function takes user input and returns a response based on user input'''
    user_input= user_input.lower()
    if any (greet in user_input for greet in['hi','hey','hello']):
        return random.choice(greeting)
    
    elif any (help in user_input for help in['help','support','assist']):
        return random.choice(help_response)
    
    elif any (joke in user_input for joke in['joke','funny','laugh']):
        return random.choice(jokes)

    elif any (fact in user_input for fact in['fact','fun fact','fun','knowledge']):
        return random.choice(facts)

    elif "your name" in user_input:
        return "My name is CHATTY! I am your first AI chatbot!"
    
    elif "what's up?" in user_input:
        return "Not much! How about you?"
    
    elif "how are you? " in user_input:
        return "I am extremely well, Thank you!\nHow do you do?"
    
    return "Sorry , I didn't get that. Can you please rephrase?"


    




## main function to run the chatbot

def chatbot():
    print("WELCOME TO CHATTY CHATBOT! I AM HERE TO HELP YOU.")
    print("TYPE  'Bye' TO EXIT")

    #run a while loop so chat never actually ends until and unless user types bye
    while True:
        user_input=input('User: ')
        if user_input.lower()=="bye":
            break
        else:
            response=chatty_response(user_input)
            print("Chatty: ",response)



#Running the chatbot

if __name__== '__main__':
    chatbot()