def solution(n, lost, reserve):
    result = [1] * (n+1)
    for i in lost:
        result[i] -=1
    for i in reserve:
        result[i] +=1

    for i in reserve:
        if i != len(result)-1 and i != 1:
            if result[i-1] == 0 or result[i+1] == 0:
                result[i] -=1
                if result[i-1] == 0:
                    result[i-1] = 1
                elif result[i+1] == 0:
                    result[i+1] = 1
        elif i == len(result) -1 :
            if result[i-1] == 0:
                result[i] -=1
                result[i-1] = 1
        elif i == 1:
            if result[i+1] == 0:
                result[i] -=1
                result[i+1] =1
    result[0] = 0
    print(result)
    count = 0
    for i in result:
        if i >= 1:
            count +=1
    answer = count
    return answer
