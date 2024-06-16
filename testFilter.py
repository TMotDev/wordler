import wordleFilter

def readFile(fileName: str):
    with open(fileName) as f:
        return f.read().splitlines()

def test_word(answer:str, words):

    yellow_letters = {}
    green_letters = {}
    gray_letters = set()

    while(len(words) > 1):
        words = wordleFilter.filterWords(words, green_letters, yellow_letters, gray_letters)
        word = words[2] if len(words) >= 3 else words[0]

        for index,c in enumerate(word):
            if c in answer and c == answer[index]:
                if c in green_letters:
                    green_letters[c].add(index)
                else:
                    green_letters[c] = {index}
            if c in answer and c != answer[index]:
                if c in yellow_letters:
                    yellow_letters[c].add(index)
                else:
                    yellow_letters[c] = {index}
            elif c not in answer:
                gray_letters.add(c)

        print(f"Trying word: {word}")
        print(f"Remaining words: {len(words)}")

    assert words[0] == answer, f"The final word {words[0]} does not match the answer {answer}"
    print(f"The answer is: {words[0]}")


if __name__ == "__main__":

    words = readFile("words.txt")

    test_word("rayon", words)
    print("---")
    test_word("train", words)
    print("---")
    test_word("razai", words)
    print("---")
