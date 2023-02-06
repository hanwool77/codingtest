def solution(today, terms, privacies):
    today = today.split(".")
    to_year, to_mon, to_day = int(today[0]), today[1], today[2]
    to_mon = int(to_mon.lstrip("0"))
    to_day = int(to_day.lstrip("0"))
    오늘 = to_year * (28 * 12) + (to_mon - 1) * 28 + to_day
    answer = []
    
    유효기간 = {}
    for term in terms:
        종류, 기간 = term.split(" ")
        유효기간[종류] = int(기간)
    print("오늘", 오늘)
    for idx, privacy in enumerate(privacies):
        시작날짜 = privacy[:10].split(".")
        s_year, s_mon, s_day = int(시작날짜[0]), 시작날짜[1], 시작날짜[2]
        s_mon = int(s_mon.lstrip("0"))
        s_day = int(s_day.lstrip("0"))
        total = s_year * (28 * 12) + (s_mon - 1) * 28 + s_day + 유효기간[privacy[-1]] * 28
        print(total)
        if total <= 오늘:
            answer.append(idx + 1)
            
    return answer