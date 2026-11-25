global wlap
wlap = 0
def p(b):
    for i in range(9):
        for j in range(9):
            if (not(type(b[i][j])==int)or b[i][j]==0):
                arr = [1,2,3,4,5,6,7,8,9]
                for k in range(9):
                    if (arr.__contains__(b[i][k])):
                        arr.remove(b[i][k])
                for k in range(9):
                    if (arr.__contains__(b[k][j])):
                        arr.remove(b[k][j])
                for p in range(3):
                    for k in range(3):
                        if (arr.__contains__(b[3*(i//3) + p][3*(j//3) + k])):
                            arr.remove(b[3*(i//3) + p][3*(j//3) + k])
                b[i][j] = arr
    return b
def blank_arr(possible):
    arr = []
    pos = []
    for i in range(9):
        for j in range (9):
            if (not(type(possible[i][j])==int)or possible[i][j]==0):
                arr.append(possible[i][j])
                pos.append([i,j])
    count = []
    for i in range(len(arr)):
        count.append(len(arr[i]))
    if arr == []:
        return [],[]
    mini= 10
    mini_index = 0
    for i in range(len(arr)):
        if mini>count[i]:
            mini = count[i]
            mini_index = i
    if (arr[mini_index] == []):
        return False
    if type(arr[mini_index])== int:
        return [arr[mini_index]], pos[mini_index]
    else:
        return arr[mini_index], pos[mini_index]
def s(b):
    global wlap
    wlap +=1
    print(wlap)
    if (blank_arr(p(b)) == False):
        return False
    arr, pos = blank_arr(p(b))
    if arr == []:
        return b
    count = 0
    for i in range(len(arr)):
        count+=1
        b[pos[0]][pos[1]] = arr[i]
        result =s(b)
        if (not(result==False)):
            return result
    if count == len(arr):
        b[pos[0]][pos[1]] = 0
        return False
board = [[0,3,0,0,0,0,2,1,4],
         [6,7,2,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [5,4,1,2,8,3,7,0,6],
         [2,0,0,4,0,6,3,5,1],
         [9,6,0,0,0,5,4,2,8],
         [0,0,0,0,0,0,6,4,5],
         [0,2,0,0,0,4,8,7,9],
         [4,9,6,0,0,0,1,3,2],]
print(s(board)) 
