def solution(citations: list) -> int:
    answer = 0
    citations.sort()
    citations.reverse()
    
    for i in range(0, len(citations)):
        answer += 1
        if (citations[i] < answer):
            return answer - 1
        elif (citations[i] == answer):
            return answer
        
    return answer