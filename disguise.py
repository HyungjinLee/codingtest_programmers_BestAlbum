import heapq
def solution(genres, plays):
    play_per_genre = {}
    answer = []
    for idx,info in enumerate(zip(genres,plays)) :
        if info[0] not in play_per_genre:
            play_per_genre[info[0]] = [(-info[1],info[1],idx)]
        else :
            heapq.heappush(play_per_genre[info[0]],(-info[1],info[1],idx))
    play_per_genre = sorted(play_per_genre.values(), key = lambda x:sum(map(lambda y:y[0],x)), reverse = True)
    
    while play_per_genre :
        item = play_per_genre.pop()
        for i in range (2) :
            if item :
                answer.append(heapq.heappop(item)[2])
    return answer