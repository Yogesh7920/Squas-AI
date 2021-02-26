from utils.speech import hear, speak


def ask(filter, options):
    speak(f"what is the {filter} you want?")
    temp = hear()
    temp = temp.lower()
    if temp in options:
        return temp
    elif "skip" in temp:
        return ""
    else:
        speak("sorry, I did not understand")
        ask(filter, options)


def interact():
    query = {}
    item = "t-shirt"

    if "t-shirt" in item.lower():

        speak("What are the filters You want to add?")
        filters = ['color', 'brand', 'fit', 'neck-line', 'apparel', 'sleeve']
        print(*filters)
        resp = hear()
        resp = resp.lower()
        while "skip" not in resp and "no" not in resp:
            if resp == "fit":
                query["fit"] = ask("fit", ['loose', 'regular', 'slim'])
            elif resp == "neck line" or resp == "neckline":
                query["neckLine"] = ask("neck line", [
                    'boat neck', 'button front', 'half zip', 'hooded', 'polo',
                    'round neck', 'shawl collar', 'sweetheart', 'v neck'])
            elif resp == "apparel":
                query["apparel"] = ask("apparel", [
                    'art silk', 'chiffon', 'corduroy', 'cotton', 'crepe',
                    'denim', 'faux fur', 'fleece', 'fur', 'georgette',
                    'leather', 'linen', 'modal', 'net', 'rayon', 'rubber',
                    'satin', 'silk', 'synthetic', 'wool'])
            elif resp == "sleeve":
                query["sleeve"] = ask("sleeve", [
                    'cap sleeve', 'half sleeve', 'long sleeve',
                    'short sleeve', 'sleeveless'])
            elif resp == "colour":
                query["colour"] = ask("colour", ['blue', 'red', 'black', 'white', 'green'])
            elif resp == "brand":
                query["brand"] = ask("brand", ['adidas', 'levis', 'arrow', 'hm', 'nike'])
            else:
                speak("sorry, I did not understand, say again")
            speak("Any additional filter you want?")
            print("These are the available filters:")
            print(*filters)
            resp = hear()
            resp = resp.lower()

    return query


if __name__ == '__main__':
    interact()
