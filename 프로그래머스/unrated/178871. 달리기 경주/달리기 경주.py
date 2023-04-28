def solution(players, callings):
    answer = []
    
    play_dict = {}
    play_line = {}
    
    for i, p in enumerate(players):
        play_dict[p] = i + 1
        play_line[i + 1] = p
        
    for call in callings:
        prev_player = play_line[play_dict[call] - 1]
        prev_line = play_dict[call] - 1
        
        now_player = call
        now_line = play_dict[call]
        
        play_line[prev_line] = now_player
        play_line[now_line] = prev_player
        
        play_dict[now_player] = prev_line
        play_dict[prev_player] = now_line
        
    for line in play_line:
        answer.append(play_line[line])
        
    return answer