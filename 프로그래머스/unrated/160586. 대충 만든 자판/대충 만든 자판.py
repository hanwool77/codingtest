INF = int(1e9)

def solution(keymap, targets):
    answer = []
    for target in targets:  # 100
        cnt = 0
        for t in target:    # 100
            min_value = INF
            for key in keymap:  # 100
                x = key.find(t)
                if x == -1:
                    continue
                min_value = min(min_value, x)
            if min_value == INF:
                cnt = -1
                break
            cnt += (min_value + 1)
        answer.append(cnt)
            
    return answer

#['AGB', "BSSS"] ["AGZ", "BSSS"]