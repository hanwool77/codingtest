def solution(babbling):
    answer = 0
    for b in babbling:
        b = b.replace("aya", ' ').replace("ye", ' ').replace("woo", ' ').replace("ma", ' ')
        if len(b.strip()) == 0:
            answer += 1
    return answer