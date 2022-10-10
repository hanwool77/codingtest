def solution(k, room_number):
    answer = []
    room = [False] * (k + 1)
    for r in room_number:
        for i in range(1, k + 1):
            if i >= r and not room[i]:
                room[i] = True
                answer.append(i)
                break
    return answer