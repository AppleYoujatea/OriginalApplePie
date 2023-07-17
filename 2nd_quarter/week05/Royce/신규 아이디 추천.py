def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    for k in new_id:
        if k.isdigit() or k.isalpha() or k in ['-', '.', '_']:
            answer += k
            
    while '..' in answer:
        answer = answer.replace('..', '.')
        # answer.replace('..', '.')로 그냥 하면 안되서 매번 갱신해주어야한다.
        
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer = '.'   # 지우는게 맞지만 뒤의 경우에서 어차피 지워질 것이다.
    if answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    
    
    return answer
