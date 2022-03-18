from django.shortcuts import render


def rating_view(main_rating, first_parameter, second_parameter, third_parameter, fourth_parameter, fifth_parameter):
    main_star = get_rating(main_rating) # суммарный рейтинг по всем параметрам
    first_star = get_rating(first_parameter)    # рейтинг по первому параметру
    second_star = get_rating(second_parameter)  # рейтинг по второму параметру
    third_parameter = get_rating(third_parameter)   # рейтинг по третьему параметру
    fourth_parameter = get_rating(fourth_parameter) # рейтинг по четвертому параметру
    fifth_parameter = get_rating(fifth_parameter)   #  рейтинг по пятому параметру
    # далее передаем все в шаблон для формирования рэйтинга


def get_rating(array):
    result = 0
    for item in array:
        result += int(item)
    result /= len(array)
    return result
