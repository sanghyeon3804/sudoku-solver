def candidates(b, i, j):
    used = set(b[i])
    for k in range(9):
        used.add(b[k][j])
        used.add(b[3*(i//3) + k//3][3*(j//3) + k%3])
    return [n for n in range(1, 10) if n not in used]


def select_blank(b):
    # 후보가 가장 적은 빈칸의 (후보, 행, 열). 빈칸이 없으면 None
    best = None
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                arr = candidates(b, i, j)
                if best is None or len(arr) < len(best[0]):
                    best = (arr, i, j)
    return best


def place(b, i, j, n):
    # 원본을 바꾸지 않고 (i, j)에 n을 넣은 새 보드를 만든다
    new = [row[:] for row in b]
    new[i][j] = n
    return new


def s(stack, calls=1):
    # stack: 아직 시도하지 않은 보드들. (보드, 나머지 스택) 형태이고 비면 None
    if stack is None:
        return False, calls - 1
    b, rest = stack
    blank = select_blank(b)
    if blank is None:
        return b, calls
    arr, i, j = blank
    for n in reversed(arr):
        rest = (place(b, i, j, n), rest)
    # 꼬리 호출: 이 뒤에 할 일이 없다. 실제 실행은 트램펄린이 한다
    return lambda: s(rest, calls + 1)


def trampoline(result):
    while callable(result):
        result = result()
    return result


def solve(b):
    # (완성된 보드 또는 False, 살펴본 보드 수)를 반환한다
    return trampoline(s((b, None)))


if __name__ == "__main__":
    board = [[0,3,0,0,0,0,2,1,4],
             [6,7,2,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [5,4,1,2,8,3,7,0,6],
             [2,0,0,4,0,6,3,5,1],
             [9,6,0,0,0,5,4,2,8],
             [0,0,0,0,0,0,6,4,5],
             [0,2,0,0,0,4,8,7,9],
             [4,9,6,0,0,0,1,3,2],]
    result, calls = solve(board)
    print(calls)
    print(result)
