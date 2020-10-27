def solution(board, moves):

    column = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board)):
            if board[j][i] != 0:
                temp.append(board[j][i])
        column.append(temp)

    bucket = []
    for i in moves:
        if len(column[i-1])>=1:
            bucket.append(column[i-1].pop(0))
    print(bucket)

    answer = 0
    temp = bucket
    for i in range(len(bucket)):
        print(len(temp))
        for j in range(1, len(temp)):
            if temp[j-1] == temp[j]:

                temp.pop(j-1)
                temp.pop(j-1)
                print(temp)
                answer+=2
                break

    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
