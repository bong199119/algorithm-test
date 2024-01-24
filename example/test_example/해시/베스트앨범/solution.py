def sort_genre(list_genre_totalplay):
    
    return list_genre_totalplay

def solution(genres, plays):
    answer = []
    dict_genres = {}
    dict_plays = {}
    list_selected = []
    list_genre_totalplay = []

    for idx, play in enumerate(plays):
        dict_plays[play] = idx

        if genres[idx] not in dict_genres:
            dict_genres[genres[idx]] = {}
            dict_genres[genres[idx]]['plays'] = [play]
            dict_genres[genres[idx]]['total plays'] = play

        else:
            dict_genres[genres[idx]]['plays'].append(play)
            dict_genres[genres[idx]]['total plays'] += play

    for genre in dict_genres:
        dict_genres[genre].sort()
        list_genre_totalplay.append([genre, dict_genres[genre]['total plays'], dict_genres[genre][-2:]])
    
    list_genre_totalplay = sort_genre(list_genre_totalplay)
    
    for genre_totalp_top2 in list_genre_totalplay:
        first = genre_totalp_top2[-1][0]
        sec = genre_totalp_top2[-1][1]
        answer.append(dict_plays[first])
        answer.append(dict_plays[sec])

    print(dict_genres)
    print(dict_plays)
    print(list_selected)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
answer = solution(genres, plays)
print(answer)

