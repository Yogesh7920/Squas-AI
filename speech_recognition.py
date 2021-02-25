from utils.speech import hear, speak


# item = 't-shirt'
def ask_for_fit():
    speak("what is the fit you want?")
    fit = hear()
    fit = fit.lower()
    options = ['loose', 'regular', 'slim']
    if (fit in options):
        return fit
    elif ("skip" in fit):
        return ""
    else:
        speak("sorry, I did not understand")
        ask_for_fit()


def ask_for_neck_line():
    speak("what is the neck line you want?")
    neckLine = hear()
    neckLine = neckLine.lower()
    options = [
        'boat neck', 'button front', 'half zip', 'hooded', 'polo',
        'round neck', 'shawl collar', 'sweetheart', 'v neck'
    ]
    if (neckLine in options):
        return neckLine
    elif ("skip" in neckLine):
        return ""
    else:
        speak("sorry, I did not understand")
        ask_for_neck_line()


def ask_for_apparel():
    speak("what is the apparel you want?")
    apparel = hear()
    apparel = apparel.lower()
    options = [
        'art silk', 'chiffon', 'corduroy', 'cotton', 'crepe',
        'denim', 'faux-fur', 'fleece', 'fur', 'georgette',
        'leather', 'linen', 'modal', 'net', 'rayon', 'rubber',
        'satin', 'silk', 'synthetic', 'wool']
    if (apparel in options):
        return apparel
    elif ("skip" in apparel):
        return ""
    else:
        speak("sorry, I did not understand")
        ask_for_apparel()


def ask_for_sleevetype():
    speak("what is the sleeve type you want?")
    sleeve = hear()
    sleeve = sleeve.lower()
    options = [
        '3/4 sleeve', 'cap sleeve', 'half sleeve', 'long sleeve',
        'short sleeve', 'sleeveless'
    ]
    if (sleeve in options):
        return sleeve
    elif ("skip" in sleeve):
        return ""
    else:
        speak("sorry, I did not understand")
        ask_for_sleevetype()


def interact():
    speak("Hi What do you want to buy?")
    item = hear()
    if ("t-shirt" in item.lower()):
        fit = ask_for_fit()
        neck_line = ask_for_neck_line()
        apparel = ask_for_apparel()
        sleeve = ask_for_sleevetype()


if __name__ == '__main__':
    interact()