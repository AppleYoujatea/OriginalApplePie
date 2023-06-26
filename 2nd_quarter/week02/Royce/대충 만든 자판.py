def solution(keymap, targets):
    answer = []
    
    # alp = []
    # 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지
    
#     // A,B,C,D에 대해 alp에 인덱스를 다 넣는다..?
#     for i in len(keymap):
#         for j in len(keymap[i]):
            
    for word in targets:
        num = 0
        
        for k in word:
            check = False
            idx = 100
            
            for h in keymap:
                if k in h:
                    idx = min(h.index(k)+1, idx)
                    check = True
            
            if not check:
                num = -1
                break
                # 불가능 하다는 뜻
    
            num += idx
        
        answer.append(num)
    
        
    return answer
