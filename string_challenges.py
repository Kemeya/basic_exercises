# Вывести последнюю букву в слове
word = 'Архангельск'
letters = list(word)
print(letters[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
letters = list(word)
print(len(letters))


# Вывести количество гласных букв в слове

# ПРОБЛЕМА:  'if' __  'not in' почему-то распознает не все согласные, пропускает их как гласные. 
# Специально перед подсчетом вывожу финальный список букв и в нем часть согласных сохраняется. 
# В то же время, если удалить из условия 'not' - то гласные идентифицируются верно и удаляются
word = 'Архангельск'
word = word.lower()
vowels = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
letters = list(word)
for consonant in letters:
    if consonant not in vowels:
        letters.remove(consonant)
print(letters)
print(len(letters))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
print(len(sentence))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for word in sentence:
    word2 = list(word)
    print(word2[0])  


# Вывести усреднённую длину слова в предложении

# Вариант №1 
sentence = 'Мы приехали в гости'
sentence = sentence.split()
len1 = len(sentence)
letters_summ = 0
for word in sentence:
    summ = len(word)
    letters_summ += summ
letters_avg = letters_summ / len1
print(letters_avg)

# Вариант №2
sentence = 'Мы приехали в гости'
sentence_1 = sentence.split()
words_summ = len(sentence_1)
sentence_2 = list(sentence)
del_element = ' '
for letter in sentence_2:
    if letter == del_element:
        sentence_2.remove(del_element)
letters_summ = len(sentence_2)  
letters_avg = letters_summ / words_summ
print(letters_avg)