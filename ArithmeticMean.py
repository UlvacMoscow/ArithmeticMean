group_students = {'student_1':
                {'name': 'Vlad', 'sername': 'Molchanov',
                 'sex': 'man', 'experience in programming': False,
                 'homework1': 6, 'homework2': 6,
                 'homework3': 9, 'homework4': 10,
                 'homework5': 5, 'exam': 7},
                  'student_2':
                {'name': 'Daria', 'sername': 'Iwanylova',
                 'sex': 'woman', 'experience in programming': False,
                 'homework1': 6, 'homework2': 9,
                 'homework3': 9, 'homework4': 10,
                 'homework5': 9, 'exam': 8},
                  'student_3':
                  {'name': 'Arsenei', 'sername': 'Abraamyan',
                   'sex': 'man', 'experience in programming': True,
                   'homework1': 6, 'homework2': 6,
                   'homework3': 9, 'homework4': 10,
                   'homework5': 10, 'exam': 5},
                  'student_4':
                  {'name': 'Sergei', 'sername': 'Kundryukov',
                   'sex': 'man', 'experience in programming': True,
                   'homework1': 10, 'homework2': 10,
                   'homework3': 9, 'homework4': 10,
                   'homework5': 5, 'exam': 8},
                  'student_5':
                  {'name': 'Anton', 'sername': 'Astrakhantsev',
                   'sex': 'man', 'experience in programming': True,
                   'homework1': 6, 'homework2': 6,
                   'homework3': 9, 'homework4': 8,
                   'homework5': 7, 'exam': 10},
                  'student_6':
                  {'name': 'Evgeniya', 'sername': 'Zadrytskaya',
                   'sex': 'woman', 'experience in programming': False,
                   'homework1': 8, 'homework2': 7,
                   'homework3': 9, 'homework4': 10,
                   'homework5': 5, 'exam': 7},
                  'student_7':
                  {'name': 'Анна', 'sername': 'Евлахина',
                   'sex': 'woman', 'experience in programming': True,
                   'homework1': 9, 'homework2': 6,
                   'homework3': 9, 'homework4': 9,
                   'homework5': 9, 'exam': 9},
                  'student_8':
                  {'name': 'Хачатур', 'sername': 'Саркисян',
                   'sex': 'man', 'experience in programming': True,
                   'homework1': 6, 'homework2': 6,
                   'homework3': 9, 'homework4': 8,
                   'homework5': 8, 'exam': 8},
                  'student_9':
                  {'name': 'Sergei', 'sername': 'Barinov',
                   'sex': 'man', 'experience in programming': False,
                   'homework1': 10, 'homework2': 10,
                   'homework3': 9, 'homework4': 10,
                   'homework5': 5, 'exam': 7},
                  'student_10':
                {'name': 'Nika', 'sername': 'Lobanova',
                 'sex': 'woman', 'experience in programming': True,
                 'homework1': 6, 'homework2': 6,
                 'homework3': 9, 'homework4': 10,
                 'homework5': 5, 'exam': 10},
                  'student_11':
                  {'name': 'Илья', 'sername': 'Мартысюк',
                   'sex': 'man', 'experience in programming': False,
                   'homework1': 5, 'homework2': 5,
                   'homework3': 5, 'homework4': 6,
                   'homework5': 5, 'exam': 6},
                  'student_12':
                  {'name': 'Mariya', 'sername': 'Tulebaeva',
                   'sex': 'woman', 'experience in programming': False,
                   'homework1': 10, 'homework2': 9,
                   'homework3': 9, 'homework4': 10,
                   'homework5': 10, 'exam': 10},
                  'student_13':
                  {'name': 'Alex', 'sername': 'Maior',
                   'sex': 'man', 'experience in programming': True,
                   'homework1': 9, 'homework2': 9,
                   'homework3': 9, 'homework4': 10,
                   'homework5': 9, 'exam': 10}
                }

def value_homeworks():
    amount_homework = 0
    for student in group_students:
        for kk in group_students[student]:
            if kk.startswith('homework'):
                if int(kk[len('homework'):len(kk)]) > amount_homework:
                    amount_homework = int(kk[len('homework'):len(kk)])
    return amount_homework


def best_of_the_best():
    best_student = 0
    best_mean_homework = 0
    for student in group_students:
        c = 0
        i = 1
        j = value_homeworks()
        while i <= j:
            c += group_students[student]['homework{}'.format(i)]
            print(c)
            if i == j:
                print("here", best_mean_homework, "c = ", c)
                if best_mean_homework <= c:
                    best_mean_homework = c
                    print(best_mean_homework)
                    print('среднее значение ',
                          round((best_mean_homework / j * 0.6 + group_students[student]['exam'] * 0.4), 2))
                    other_best_student = round((best_mean_homework / j * 0.6 + group_students[student]['exam'] * 0.4), 2)
                    if best_student >= other_best_student:
                        print('Лучшие студенты')
                    best_student = round((best_mean_homework / j * 0.6 + group_students[student]['exam'] * 0.4), 2)
            i += 1
        return print('Лучший студент {} {} c интегральной оценкой {}'.format(
            group_students[student]['name'], group_students[student]['sername'], best_student))


def arithmetic_mean_on_group():
    sum_all_group = 0
    k = 0
    j = value_homeworks()
    for student in group_students:
        i = 1
        while i <= j:
            sum_all_group += group_students[student]['homework{}'.format(i)]
            i += 1
            k += 1
    print('Средняя оценка за домашние задания по группе: X = ', round(sum_all_group/k, 2))


def exam_mean_on_group():
    sum_all_group = 0
    k = 0
    for student in group_students:
        sum_all_group += group_students[student]['exam']
        k += 1
    print('Средняя оценка за экзамен: Y = ', round(sum_all_group/k, 2))


def man_group_mean_result(param, value):
    k = 0
    sum_all_group = 0
    j = value_homeworks()
    for student in group_students:
        if group_students[student][param] == value:
            i = 1
            while i <= j:
                sum_all_group += group_students[student]['homework{}'.format(i)]
                i += 1
                k += 1
    return round(sum_all_group/k, 2)


def man_group_mean_result_exams(param, value):
    k = 0
    sum_all_group = 0
    for student in group_students:
        if group_students[student][param] == value:
            sum_all_group += group_students[student]['exam']
            k += 1
    return round(sum_all_group/k, 2)


while True:
    use_command = input(
        "Введите одну из следующих команд:"
        " \n ""Средняя оценка за домашние задания по группе: \"X\""
        " \n Средняя оценка за экзамен:  \"Y\"\n "
        "Средняя оценка за домашние задания у мужчин:"
        " \"A\"\n Средняя оценка за экзамен у мужчин: \"B\"\n "
        "Средняя оценка за домашние задания у женщин: \"C\" \n "
        "Средняя оценка за экзамен у женщин: \"D\"  \n Средняя "
        "оценка за домашние задания у студентов с опытом: \"E\""
        " \n Средняя оценка за экзамен у студентов с опытом: \"F\" \n"
        " Средняя оценка за домашние задания у студентов без опыта: \"G\""
        " \n Средняя оценка за экзамен у студентов без опыта: \"H\" \n "
        "quit(введите \"q\") - выход;\n")

    if use_command.upper() == 'A':
        print('Средняя оценка за домашние задания у мужчин:'
              ' A = {}'.format(man_group_mean_result('sex', 'man')))
    if use_command.upper() == "B":
        print('Средняя оценка за экзамен у мужчин:'
              ' B = {}'.format(man_group_mean_result_exams('sex', 'man')))
    if use_command.upper() == "C":
        print('Средняя оценка за домашние задания у женщин:'
              ' C = {}'.format(man_group_mean_result('sex', 'woman')))
    if use_command.upper() == "D":
        print('Средняя оценка за экзамен у женщин:'
              ' D = {}'.format(man_group_mean_result_exams('sex', 'woman')))
    if use_command.upper() == "E":
        print("Средняя оценка за домашние задания у студентов с опытом:  E ="
              " {}".format(man_group_mean_result('experience in programming', True)))
    if use_command.upper() == "F":
        print("Средняя оценка за экзамен у студентов с опытом: F ="
              " {}".format(man_group_mean_result_exams('experience in programming', True)))
    if use_command.upper() == "G":
        print("Средняя оценка за домашние задания у студентов без опытом:  G ="
              " {}".format(man_group_mean_result('experience in programming', False)))
    if use_command.upper() == "H":
        print("Средняя оценка за экзамен у студентов с опытом: H ="
              " {}".format(man_group_mean_result_exams('experience in programming', False)))
    if use_command.upper() == "X":
        arithmetic_mean_on_group()
    if use_command.upper() == "Y":
        exam_mean_on_group()
    if use_command.upper() == "S":
        best_of_the_best()
    if use_command.upper() == "Q":
        break

