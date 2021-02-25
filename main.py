from utils.others import api
import random
from AI import AI
import speech_ai as sr 
from utils.speech import hear, speak
import os

if __name__ == '__main__':
    speak("Welcome to Squas T Shirts Virtual Showroom")
    speak("what is the user name?")
    username = hear()
    username = username.lower()
    while(username not in ['yogesh', 'gurunadh', 'mitul']):
        speak("User does not exit in database")
        username = hear()
        username = username.lower()
    
    if(os.path.exists(os.path.join("users", username + ".h5"))):
        mode = 'production'
    else:
        mode = 'development'

    
    query = sr.interact()


    query ['item'] = 't-shirt'
    print(query)
    data = api(**query)
    if not data:
        # print("no data for ur query")
        speak("sorry, No products available for your requirement")
        
    else:

        if mode == 'development':
            ai = AI(username, 'rec')
            ai.train(data)
            test_data = random.sample(data, 50)
            ai.test(test_data)
        else:
            ai = AI(username, 'bin')
            best_prod = ai.predict(data)
            print(best_prod)
            correct = int(input("Is this prediction correct (1/0)"))

            if not correct:
                ai.feedback_train([best_prod], username)
