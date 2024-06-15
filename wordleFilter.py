# def filterWords(words: list[str], green_letters: dict[str, set[int]], yellow_letters: dict[str, set[int]], gray_letters: set[str]) -> list[str]:
#     """
#     Filters a list of words based on specified letter constraints, similar to the rules of the game "Wordle".

#     Parameters:
#     ----------
#     words : list of str
#         The list of words to be filtered.
#     green_letters : dict of str : list of int
#         A dictionary where the keys are letters that must appear in specific positions
#         in the words. The values are lists of indices (0-based) specifying the required positions.
#     yellow_letters : dict of str : list of int
#         A dictionary where the keys are letters that must appear in the words but not
#         in specific positions. The values are lists of indices (0-based) specifying the positions
#         where these letters must not appear.
#     gray_letters : set of str
#         A set of letters that must not appear in the words.

#     Returns:
#     -------
#     list of str
#         A list of words that satisfy all the given constraints.

#     Notes:
#     -----
#     - A word is included in the result if and only if it contains all green letters
#       at the specified positions, contains all yellow letters but not in the specified positions,
#       and does not contain any gray letters.
#     - If a word fails any of these checks, it is excluded from the result.

#     Example:
#     -------
#     >>> words = ["tiger", "truer", "track", "trust"]
#     >>> green_letters = {'t': [4]}
#     >>> yellow_letters = {'r': [1, 2, 4], 'u': [1]}
#     >>> gray_letters = set('wiemods')
#     >>> filterWords(words, green_letters, yellow_letters, gray_letters)
#     {'trust'}
#     """

#     filteredWords = list()

#     for word in words:

#         # Check for gray letters, unless overridden by green or yellow letters
#         gray_flag = False
#         for index, c in enumerate(word):
#             if c in gray_letters:
#                 if index not in green_letters.get(c, []) and index not in yellow_letters.get(c, []):
#                     gray_flag = True
#                     break
#         if gray_flag:
#             continue

#         # Check for green letters
#         green_flag = True
#         for c, indices in green_letters.items():
#             for index in indices:
#                 if word[index] != c:
#                     green_flag = False
#                     break
#             if not green_flag:
#                 break

#         if not green_flag:
#             continue

#         # Check for yellow letters in wrong positions
#         yellow_flag = True
#         for c, indices in yellow_letters.items():
#             for index in indices:
#                 if word[index] == c:
#                     yellow_flag = False
#                     break
#             if not yellow_flag:
#                 break

#         if not yellow_flag:
#             continue

#         # Ensure yellow letters are present but not in the specified positions
#         yellow_flag = True
#         for c, indices in yellow_letters.items():
#             if c not in word:
#                 yellow_flag = False
#                 break
#             for index in indices:
#                 if word[index] == c:
#                     yellow_flag = False
#                     break
#             if not yellow_flag:
#                 break

#         if not yellow_flag:
#             continue

#         filteredWords.append(word)

#     return filteredWords


def filterWords(words: list[str], green_letters: dict[str, set[int]], yellow_letters: dict[str, set[int]], gray_letters: set[str]) -> list[str]:
    """
    Filters a list of words based on specified letter constraints, similar to the rules of the game "Wordle".

    Parameters:
    ----------
    words : list of str
        The list of words to be filtered.
    green_letters : dict of str : set of int
        A dictionary where the keys are letters that must appear in specific positions
        in the words. The values are sets of indices (0-based) specifying the required positions.
    yellow_letters : dict of str : set of int
        A dictionary where the keys are letters that must appear in the words but not
        in specific positions. The values are sets of indices (0-based) specifying the positions
        where these letters must not appear.
    gray_letters : set of str
        A set of letters that must not appear in the words.

    Returns:
    -------
    list of str
        A list of words that satisfy all the given constraints.

    Notes:
    -----
    - A word is included in the result if and only if it contains all green letters
      at the specified positions, contains all yellow letters but not in the specified positions,
      and does not contain any gray letters.
    - If a word fails any of these checks, it is excluded from the result.

    Example:
    -------
    >>> words = ["tiger", "truer", "track", "trust"]
    >>> green_letters = {'t': [4]}
    >>> yellow_letters = {'r': [1, 2, 4], 'u': [1]}
    >>> gray_letters = set('wiemods')
    >>> filterWords(words, green_letters, yellow_letters, gray_letters)
    {'trust'}
    """
    filteredWords = []

    for word in words:
        # Check for gray letters, unless overridden by green or yellow letters
        gray_flag = False
        for index, c in enumerate(word):
            if c in gray_letters and (index not in green_letters.get(c, set())) and (index not in yellow_letters.get(c, set())):
                gray_flag = True
                break
        if gray_flag:
            continue

        # Check for green letters
        green_flag = True
        for c, indices in green_letters.items():
            for index in indices:
                if word[index] != c:
                    green_flag = False
                    break
            if not green_flag:
                break
        if not green_flag:
            continue

        # Check for yellow letters not in the specified positions
        yellow_flag = True
        for c, indices in yellow_letters.items():
            # Ensure yellow letters are present
            if c not in word:
                yellow_flag = False
                break

            # Ensure yellow letters are not in the specified positions
            for index in indices:
                if word[index] == c:
                    yellow_flag = False
                    break
            if not yellow_flag:
                break

        if not yellow_flag:
            continue

        filteredWords.append(word)

    return filteredWords