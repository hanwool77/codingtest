import sys

sys.setrecursionlimit(10 ** 7)


def find_empty_room(r, room):
    if r not in room:  # 배장된 방이 비어있으면
        # 배정된 방보다 번호가 크면서 비어있는 방 중 번호가 가장 작은 방을 가리키도록 저장
        room[r] = r + 1
        return r
    else:  # 이미 배정되있다면
        # 배정할 방을 새로 찾음
        nr = find_empty_room(room[r], room)
        # 배정된 방보다 번호가 크면서 비어있는 방 중 번호가 가장 작은 방을 가리키도록 저장
        room[r] = nr + 1
        return nr


def solution(k, room_number):
    answer = []
    room = dict()
    for r in room_number:
        answer.append(find_empty_room(r, room))
    return answer