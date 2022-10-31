def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'
          , 'nine']
    for num, e in enumerate(eng):
        if e in s:
            s = s.replace(e, str(num))
    return int(s)