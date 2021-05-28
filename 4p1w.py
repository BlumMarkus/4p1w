import re

letterAmount = input('Buchstaben-Anzahl: ')
availableLetter = input('Verfügbare Buchstaben: ').lower()

pattern = re.compile('[' + availableLetter + availableLetter.upper() + ']{' + letterAmount + '}')

dictionaryFile = letterAmount + '.txt'
with open(dictionaryFile, 'r') as completeDictionary:
    dictionary = completeDictionary.read()

    matches = pattern.finditer(dictionary)

    for match in matches:
        word = match.group(0)
        lowerLetters = word.lower()

        i = 0
        wordFits = True
        while i < 12:
            if lowerLetters.count(availableLetter[i]) > availableLetter.count(availableLetter[i]):
                wordFits = False
            i += 1

        if wordFits:
            print(word)
