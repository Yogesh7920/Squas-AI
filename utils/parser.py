from matplotlib import colors


def sizechart_tshirt(name, size):
    # From Levi's shirt sizechart measurements
    # return format [chest, shoulder width, Front length] in cms
    return {
        'adidas': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'levis': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'arrow': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'hm': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'nike': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
    }.get(name, -1).get(size, -1)


def sizechart_shoe(brand, size):
    # Convert shoe size from UK/IN to Foot Length (in cm)
    return {
        'adidas': {
            '6': [23.7],
            '7': [25.4],
            '8': [26.2],
            '9': [27.1],
            '10': [27.9],
            '11': [28.8],
        },
        'nike': {
            '6': [23.7],
            '7': [25.4],
            '8': [26.2],
            '9': [27.1],
            '10': [27.9],
            '11': [28.8],
        },
        'puma': {
            '6': [23.7],
            '7': [25.4],
            '8': [26.2],
            '9': [27.1],
            '10': [27.9],
            '11': [28.8],
        },
        'levis': {
            '6': [23.7],
            '7': [25.4],
            '8': [26.2],
            '9': [27.1],
            '10': [27.9],
            '11': [28.8],
        },
        'arrow': {
            '6': [23.7],
            '7': [25.4],
            '8': [26.2],
            '9': [27.1],
            '10': [27.9],
            '11': [28.8],
        },
    }.get(brand, -1).get(size, -1)


def sizechart_bra(name, size):
    return {
        'jockey': {
            'XS': [67],
            'S': [77],
            'M': [87],
            'L': [97],
            'XL': [107],
            'XXL': [117],
        },
        'enamor': {
            'XS': [81],
            'S': [86],
            'M': [91],
            'L': [96],
            'XL': [101]
        },
        'triumph': {
            'XS': [82],
            'S': [87],
            'M': [92],
            'L': [97],
            'XL': [102],
        },
        'Calvin Klein': {
            'XS': [82],
            'S': [87],
            'M': [92],
            'L': [97],
            'XL': [103],

        },

    }.get(name, -1).get(size, -1)


def colourencoding(colour):
    """
    We will add coding into RGB values thus making more reasonable encoding
    :param colour:
    :return: RGB
    """
    # print(colour)
    return dict(zip(('R', 'G', 'B'), colors.to_rgb(colour)))
    # return {'R': 0, 'B': 255, 'G': 0}


def brandencoding(brand):
    return {
        'adidas': 0,
        'levis': 1,
        'arrow': 2,
        'hm': 3,
        'nike': 4,
        'puma': 3,
        'jockey': 0,
        'enamor': 1,
        'triumph': 2
    }.get(brand, -1)


def categoryencoding(category):
    return {
        't-shirt': 0,
        'tshirt': 0,
        'bra': 1,
        'shoe': 2
    }.get(category, -1)

def fitencoding(fit):
    return{
        'loose': 0,
        'regular': 1,
        'slim': 2,
    }.get(fit, -1)

def sleeveencoding(sleeveType):
    return {
        '3/4-sleeve': 0,
        'cap-sleeve': 1,
        'half-sleeve': 2,
        'long-sleeve': 3,
        'short-sleeve': 4,
        'sleeveless': 5,
    }.get(sleeveType, -1)

def neckLineencoding(name):
    return {
        'Boat-Neck': 0,
         'button-front': 1,
         'half-zip': 2,
         'hooded': 3,
         'polo': 4,
         'round-neck': 5,
         'shawl-collar': 6,
         'sweetheart': 7,
         'v-neck': 8
    }.get(name, -1)

def encode(key, val, brand, name):
    if key == 'item':
        return categoryencoding(val)
    elif key == 'size':
        if name == 't-shirt' or name == 'tshirt':
            return sizechart_tshirt(brand, val)
        elif name == 'shoe':
            return sizechart_shoe(brand, val)
        elif name == 'bra':
            return sizechart_bra(brand, val)
        else:
            return val
    elif key == 'brand':
        return brandencoding(val)
    elif key == 'fit':
        return fitencoding(val)
    elif key == 'sleeveType':
        return sleeveencoding(val)
    else:
        return val


def parser(raw_data):
    prod_attr = []
    for data in raw_data:
        dict = {}
        brand = data['brand']
        name = data['item']
        for key, val in data.items():
            dict[key] = encode(key, val, brand , name)
        dict = {**dict, **colourencoding(dict.pop('colour', None))}
        prod_attr.append(dict)
    return prod_attr
