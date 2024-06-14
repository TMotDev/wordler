import wordleFilter

def readFile(fileName: str):
    with open(fileName) as f:
        return f.read().splitlines()


def main():

    words = readFile("five_char_words.txt")
    yellow_letters: dict[str, list] = {}
    green_letters: dict[str, list] = {'r':[0],'e':[1]}
    gray_letters = set("stabidflycur")


    result = wordleFilter.filterWords(words, green_letters, yellow_letters, gray_letters)
    print(result)


if __name__ == "__main__":
    main()
