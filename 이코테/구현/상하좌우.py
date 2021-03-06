# n입력받기
n = int(input())
x, y = 1, 1 # 시작 점
plans = input().split() # 이동할 계획 입력받기

#L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1] # 지정 자유로 가능
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)

