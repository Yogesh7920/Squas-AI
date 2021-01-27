import requests
import numpy as np

if __name__ == '__main__':
    name = 't-shirt'
    url = 'https://squas-store.herokuapp.com/amazon/'

    for i in range(300):
        price = np.random.randint(4, 11) * 100
        size = np.random.choice(['S', 'M', 'L'])
        rating = round(np.random.uniform(3.5, 5), 1)
        num_of_reviews = np.random.randint(500, 1500)
        brand = np.random.choice(['nike', 'adidas', 'hm', 'levis', 'arrow'])
        discount = round(np.random.uniform(0, 40))
        colour = np.random.choice(['blue', 'red', 'black', 'white', 'gray', 'yellow'])

        d = {
            'name': name,
            'price': price,
            'size': size,
            'rating': rating,
            'num_of_reviews': num_of_reviews,
            'brand': brand,
            'discount': discount,
            'colour': colour
        }

        r = requests.post(url, data=d)
        print(i, r.status_code)

