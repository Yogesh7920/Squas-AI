import requests
import numpy as np

if __name__ == '__main__':
    name = 't-shirt'
    url = 'https://squas-store.herokuapp.com/amazon/'

    for i in range(500):
        price = np.random.randint(6, 18) * 50
        size = np.random.choice(['XS', 'S', 'M', 'L', 'XL'])
        rating = round(np.random.uniform(1, 5), 1)
        num_of_reviews = np.random.randint(500, 1500)
        brand = np.random.choice(['adidas', 'levis', 'arrow', 'hm', 'nike'])
        discount = round(np.random.uniform(5, 50))
        colour = np.random.choice(['blue', 'red', 'black', 'white', 'green'])
        neckLine = np.random.choice([
            'boat neck', 'button front', 'half zip', 'hooded', 'polo',
            'round neck', 'shawl collar', 'sweetheart', 'v neck'
        ])
        fit = np.random.choice(['loose', 'regular', 'slim'])
        apparel = np.random.choice([
            'art silk', 'chiffon', 'corduroy', 'cotton', 'crepe',
            'denim', 'faux fur', 'fleece', 'fur', 'georgette',
            'leather', 'linen', 'modal', 'net', 'rayon', 'rubber',
            'satin', 'silk', 'synthetic', 'wool'])
        sleeveType = np.random.choice([
            'cap sleeve', 'half sleeve', 'long sleeve',
            'short sleeve', 'sleeveless'
        ])
        deal = np.random.choice([True, False], p=[0.1, 0.9])

        d = {
            'item': name,
            'price': price,
            'size': size,
            'rating': rating,
            'num_of_reviews': num_of_reviews,
            'brand': brand,
            'discount': discount,
            'colour': colour,
            'neckLine': neckLine,
            'fit': fit,
            'apparel': apparel,
            'sleeveType': sleeveType,
            'deal': deal
        }

        r = requests.post(url, data=d)
        print(i, r.status_code)

# import requests
# import numpy as np

# if __name__ == '__main__':
#     name = 't-shirt'
#     url = 'https://squas-store.herokuapp.com/amazon/'

#     for i in range(300):
#         price = np.random.randint(6, 18) * 50
#         size = np.random.choice(['XS', 'S', 'M', 'L', 'XL'])
#         rating = round(np.random.uniform(1, 5), 1)
#         num_of_reviews = np.random.randint(500, 1500)
#         brand = np.random.choice(['jockey', 'enamor', 'triumph'])
#         discount = round(np.random.uniform(5, 50))
#         colour = np.random.choice(['blue', 'red', 'black', 'white', 'green'])

#         d = {
#             'name': name,
#             'price': price,
#             'size': size,
#             'rating': rating,
#             'num_of_reviews': num_of_reviews,
#             'brand': brand,
#             'discount': discount,
#             'colour': colour
#         }

#         r = requests.post(url, data=d)
#         print(i, r.status_code)
