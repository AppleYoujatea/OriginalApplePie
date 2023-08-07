
def time_def(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m


def solution(book_time):
    answer = 0
    
    
    arr = sorted([[time_def(k[0]), time_def(k[1]) + 10] for k in book_time])
    # 예약이 빠른 순으로 정렬
    
    
    # 방 배정하기
    room = []
    
    for k in arr:
        if not room:
            room.append(k)
            continue
        # enumerate를 쓰면 (idx, 값)
        for idx, bed in enumerate(room):
            if k[0] >= bed[-1]:
                room[idx] = bed + k
                break
        else:
            room.append(k)
        # 안되는 경우 room을 추가한다.
        
    
    return len(room)
