import wordleFilter


def readFile(fileName: str):
    with open(fileName) as f:
        return f.read().splitlines()

def test_word(word:str, words):

    yellow_letters = {}
    green_letters = {}
    gray_letters = set()

    while(len(words) > 1):
        words = wordleFilter.filterWords(words, green_letters, yellow_letters, gray_letters)
    #TODO learn2test


if __name__ == "__main__":

    words = readFile("words.txt")

    test_word("rayon", words)