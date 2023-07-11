def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))
    # 각 유저를 신고한 리스트
    board = {id: [] for id in id_list}
    mail = {id: 0 for id in id_list}
    
    for i in report:
        u, s = i.split()
        board[s].append(u)
    
    for i in id_list:
        if len(board[i]) >= k:
            for j in board[i]:
                mail[j] += 1 
                
    for i in id_list:
        answer.append(mail[i])    

    return answer
