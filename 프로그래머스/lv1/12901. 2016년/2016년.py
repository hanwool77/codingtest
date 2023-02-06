def solution(a, b):
    answer = ''
    month = {
        1:31,
        2:29,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    요일 = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    
    day = 0
    for i in range(a - 1):
        day += month[i + 1]
    day += b
    print(day % 7)
    return 요일[day % 7]