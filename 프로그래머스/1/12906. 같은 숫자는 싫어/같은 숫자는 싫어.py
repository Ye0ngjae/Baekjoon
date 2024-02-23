def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if(i == 0):
            answer.append(arr[i])
        else:
            temp = arr[i-1]
            if(temp == arr[i]):
                continue
            else:
                answer.append(arr[i])
    
    return answer