with open('german.txt', 'r', encoding="utf8") as completeDictionary:
    completeContent = completeDictionary.readlines()

    for word in completeContent:
        word = word.replace('\n', '')
        word = word.replace(' ', '')
        word = word.replace('ae', 'ä')
        word = word.replace('oe', 'ö')
        word = word.replace('ue', 'ü')
        word = word.replace('eü', 'eue')

        wordLength = str(len(word))
        fileName = wordLength + '.txt'

        file = open(fileName, 'a')
        file.write(word + '\n')
        file.close()

        print(word + ' > ' + fileName)
