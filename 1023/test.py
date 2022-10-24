# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if(mid == 0 or array[mid - 1] < target) and array[mid] == target:
        return mid

def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0반환

    # x가 마지막으로 등장한 인덱스 계산
    b = first(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1