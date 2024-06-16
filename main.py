import wordleFilter
from rich.prompt import Prompt, IntPrompt, Confirm
from rich import print, box
from rich.table import Table
from rich.console import Console
from rich.columns import Columns

console = Console()

def readFile(fileName: str):
    with open(fileName) as f:
        return f.read().splitlines()


def update_letter_dict(input_word: str, digits: set[int], letters: dict[str, set]):
    for digit in digits:
        position = digit
        if position < len(input_word):
            char = input_word[position]
            if char in letters:
                letters[char].add(position)
            else:
                letters[char] = {position}
    return letters


def generateTable(greenIndices, yellowIndices, input):
    table = Table(box=box.MINIMAL, row_styles="bold")
    for i in range(5):
        style = "grey39"
        if i in greenIndices:
            style = "bold green"
        elif i in yellowIndices:
            style = "bold yellow"
        table.add_column(str(i+1), justify="center",
                            header_style=style)

    row = []
    for index, i in enumerate(input):
        if index in greenIndices:
            row.append(f"[bold green]{i}[/bold green]")
        elif index in yellowIndices:
            row.append(f"[bold yellow]{i}[/bold yellow]")
        else:
            row.append(i)

    table.add_row(*row, style="bold")
    return table

def gameloop(words: list[str]):

    yellow_letters = {}
    green_letters = {}
    gray_letters = set()

    show_all_available_words = Confirm.ask("Show all suggested words?", default=False)
    console.clear()
    while True and len(words) > 1:
        input = Prompt.ask("Input 5 character word:", default="-1")

        if input == "-1":
            break

        if len(input) != 5:
            print("Invalid input. Please enter a 5 character word.")
            continue

        yellowIndices = set()
        greenIndices = set()

        table = Table(box=box.MINIMAL)
        for i in range(5):
            table.add_column(str(i+1), justify="center",
                             header_style="grey39")
        table.add_row(*input)

        console.clear()
        console.rule("Wordle helper")
        console.print(table, justify="center")

        yellowInput = IntPrompt.ask(
            "Enter positions of [yellow]yellow[/] letters", default=-1)

        # update the dictionary with yellow characters
        if yellowInput > 0:
            for digit in str(yellowInput):
                digit = int(digit)-1
                if 0 <= digit <= 5:
                    yellowIndices.add(digit)
            yellow_letters = update_letter_dict(
                input, yellowIndices, yellow_letters)

        console.clear()
        console.rule("Wordle helper")
        table = generateTable(greenIndices, yellowIndices, input)
        console.print(table, justify="center")

        greenInput = IntPrompt.ask(
            "Enter positions of [green]green[/] letters", default=-1)

        # update the dictionary with green characters
        if greenInput > 0:
            for digit in str(greenInput):
                digit = int(digit)-1
                if 0 <= digit <= 5:
                    greenIndices.add(digit)
            greenIndices.difference_update(yellowIndices)
            green_letters = update_letter_dict(
                input, greenIndices, green_letters)

        grayInput = {0, 1, 2, 3, 4}.difference(greenIndices, yellowIndices)

        for i in grayInput:
            gray_letters.add(input[i])

        console.clear()
        console.rule("Wordle helper")
        table = generateTable(greenIndices, yellowIndices, input)
        console.print(table, justify="center")

        words = wordleFilter.filterWords(words, green_letters, yellow_letters, gray_letters)

        # print available words
        console.print(f"{words[:15]} {f"+ {len(words)-15} more" if len(words) > 15 else ""}", justify="center")

        if show_all_available_words:
            column = Columns(words, equal=True, expand=True)
            console.print(column, justify="center")



def main():
    words = readFile("words.txt")

    gameloop(words)

    while Confirm.ask("Start a new game?", default=True):
        gameloop(words)



if __name__ == "__main__":
    main()
