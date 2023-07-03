# def solution(survey, choices):
#     answer = ''
    
#     board = {"R": 0, "T": 0,
#              "C": 0, "F": 0,
#              "J": 0, "M": 0,
#              "A": 0, "N": 0
#             }
    
#     score = [0,3,2,1,0,1,2,3]
    
#     for i in range(len(survey)):
#         up, down = survey[i]
#         if choices[i] < 4:
#             board[up] += score[i]
#         else:
#             board[down] += score[i]
        
#     if board["R"] >= board["T"]:
#         answer += "R"
#     else:
#         answer += "T"
        
#     if board["C"] >= board["F"]:
#         answer += "C"
#     else:
#         answer += "F"
        
        
#     if board["J"] >= board["M"]:
#         answer += "J"
#     else:
#         answer += "M"
        
#     if board["A"] >= board["N"]:
#         answer += "A"
#     else:
#         answer += "N"
    
#     return answer


def solution(survey, choices):
    answer = ''
    
    board = {"R": 0, "T": 0,
             "C": 0, "F": 0,
             "J": 0, "M": 0,
             "A": 0, "N": 0
            }
    
    score = [0,3,2,1,0,1,2,3]
    
    for i in range(len(survey)):
        up, down = survey[i]
        if choices[i] <= 4:
            board[up] += score[choices[i]]
        else:
            board[down] += score[choices[i]]
        
    if board["R"] >= board["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if board["C"] >= board["F"]:
        answer += "C"
    else:
        answer += "F"
        
        
    if board["J"] >= board["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if board["A"] >= board["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer
