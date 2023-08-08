"""
풀이 시간: 08:58 ~

시작 시간 순으로 정렬
가장 빠른 방의 종료 시간 + 10 > 다음으로 빠른 방의 시작 시간이라면 answer += 1

"""

import heapq

def solution(book_time):
    # 예약을 시작 시간으로 정렬
    book_time.sort(key=lambda x: x[0])

    # 첫 번째 예약의 종료 시간을 우선순위 큐에 추가
    rooms = [book_time[0][1]]

    for i in range(1, len(book_time)):
        # 현재 예약의 시작 시간
        start_time = book_time[i][0]
        # 가장 빠른 종료 시간
        earliest_end_time = rooms[0]

        # 청소 시간을 고려한 종료 시간
        end_hour, end_min = map(int, earliest_end_time.split(":"))
        end_time_plus10 = end_hour * 60 + end_min + 10

        # 시작 시간
        start_hour, start_min = map(int, start_time.split(":"))
        start_time = start_hour * 60 + start_min

        # 청소 시간을 고려한 종료 시간이 시작 시간보다 빠르면, 같은 객실을 사용할 수 있음
        if end_time_plus10 <= start_time:
            heapq.heappop(rooms)

        # 현재 예약의 종료 시간을 우선순위 큐에 추가
        heapq.heappush(rooms, book_time[i][1])

    # 필요한 객실 수는 우선순위 큐의 크기와 같음
    return len(rooms)

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))
