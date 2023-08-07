def solution(numbers, hand):
    answer = ''
    
    arr = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}
    
    left = [1,4,7]
    right = [3,6,9]
    hand_l = '*'
    hand_r = '#'
    
    for k in numbers:
        if k in left:
            answer += 'L'
            hand_l = k
        elif k in right:
            answer += 'R'
            hand_r = k
        else:
            now = arr[k] # 와 같이 하면 arr[k]이므로 k에 맞는 (x,y)가 나옴
            left_now = arr[hand_l]
            right_now = arr[hand_r]
            left_dist = abs(now[0] - left_now[0]) + abs(now[1] - left_now[1])
            right_dist = abs(now[0] - right_now[0]) + abs(now[1] - right_now[1])
            # 길이를 그냥 이런 맨하탄 거리로 계산해주면 된다.
            
            if left_dist < right_dist:
                answer += 'L'
                hand_l = k
            elif left_dist > right_dist:
                answer += 'R'
                hand_r = k
            else:
                if hand == 'left':
                    answer += 'L'
                    hand_l = k
                else:
                    answer += 'R'
                    hand_r = k
    
    
    return answer
