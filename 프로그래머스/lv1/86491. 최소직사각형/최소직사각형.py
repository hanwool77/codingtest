def solution(sizes):
    width = height = 0
    
    for size in sizes:
        size.sort()
        width = max(width, size[0])
        height = max(height, size[1])
    
    return width * height