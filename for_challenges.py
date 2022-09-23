# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)



# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    ABC = len(name)
    print(f'{name}: {ABC}')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name, sex in is_male.items():
    if sex == True:
        is_male[name] = 'мужской'
    else:
        is_male[name] = 'женский'

print(is_male)




# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
groups_qty = len(groups)
 
if groups_qty == 1:
    groups_qty_text = 'группа'
elif groups_qty > 1:
    groups_qty_text = 'группы'
elif groups_qty > 4:
    groups_qty_text = 'групп' 
elif groups_qty > 20:
    print('Error!\nПри колличестве групп больше 20 логика склонения существительного "группа" идет на второй и последующие круги, повторяясь каждый десяток.\nАвтор слишком юн и неопытен в вопросах написания кода, чтобы реализовать такое в рамках ДЗ')   

print(f'Всего {groups_qty} {groups_qty_text}.')


pupil_num_1 = len(groups[0])

pupil_num_2 = len(groups[1])

pupil_num_3 = len(groups[2])

def the_ending(pupil_num):
    if pupil_num == 1:
        pupil_num_text = 'ученик'
    elif pupil_num > 1:
        pupil_num_text = 'ученика'
    elif pupil_num > 4:
        pupil_num_text = 'учеников'   
    elif pupil_num > 20:
            print('Error!\nПри колличестве учеников больше 20 логика склонения существительного "ученики" идет на второй и последующие круги, повторяясь каждый десяток.\nАвтор слишком юн и неопытен в вопросах написания кода, чтобы реализовать такое в рамках ДЗ')   
    return pupil_num_text 

the_ending_1 = the_ending(pupil_num_1)
the_ending_2 = the_ending(pupil_num_2)
the_ending_3 = the_ending(pupil_num_3)


print(f'Группа 1: {pupil_num_1} {the_ending_1}')
print(f'Группа 2: {pupil_num_2} {the_ending_2}')
print(f'Группа 3: {pupil_num_3} {the_ending_3}')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
# способ №1
dict = {
    'Группа 1': list(groups[0]), 
    'Группа 2' : list(groups[1]), 
    'Группа 3' : list(groups[2])
    }
for key in dict:
    value = ', '.join(dict[key])     
    print(f'{key}: {value}')

# способ №2 но он выводит без запятых между именами
groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
 # пыталась преобразовать список в строки, добавить в них запятые и снова собрать в список, но запятые после сборки в список исчезают 
 # for line in groups:
    # line = ',, '.join(line)
    # line = line.split(',')
    # print(line)
    # print(type(line))

line_with_no_comma_1 = groups[0] 
line_with_no_comma_1.insert(0, 'Группа 1:')

line_with_no_comma_2 = groups[1]
line_with_no_comma_2.insert(0, 'Группа 2:')

line_with_no_comma_3 = groups[2]
line_with_no_comma_3.insert(0, 'Группа 3:')
for line in groups:
    line = ' '.join(line)
    print(line)