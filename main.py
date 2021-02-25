from utils.others import api
import random
from AI import AI


if __name__ == '__main__':
    # mode = 'development'
    mode = 'production'
    username = 'Yogesh'
    data = api(item='t-shirt')
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
