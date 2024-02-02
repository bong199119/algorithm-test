def sort_genres(list_genre, dict_genres):
    for i in range(len(list_genre) - 1):
        for j in range(len(list_genre) - i - 1):
            if dict_genres[list_genre[j]] > dict_genres[list_genre[j+1]]:
                list_genre[j], list_genre[j+1] = list_genre[j+1], list_genre[j]
    
    return list_genre

def sort_plays(list_plays):
    for i in range(len(list_plays) - 1):
        for j in range(len(list_plays) - i - 1):
            if list_plays[j][0] > list_plays[j+1][0]:
                list_plays[j], list_plays[j+1] = list_plays[j+1], list_plays[j]

    return list_plays

def solution(genres, plays):
    answer = []
    dict_genres = {}
    list_genre = []

    for idx, play in enumerate(plays):
        if genres[idx] not in dict_genres:
            list_genre.append(genres[idx])
            dict_genres[genres[idx]] = {}
            dict_genres[genres[idx]]['plays'] = [[play, idx]]
            dict_genres[genres[idx]]['total plays'] = play

        else:
            dict_genres[genres[idx]]['plays'].append([play, idx])
            dict_genres[genres[idx]]['total plays'] += play

    list_genre_sorted = sort_genres(list_genre, dict_genres)

    for genre in list_genre_sorted:
        list_plays = dict_genres[genre]['plays']
        list_plays = sort_plays(list_plays)

        if len(list_plays) > 1:
            first_idx = list_plays[0][1]
            second_idx = list_plays[1][1]
            
            answer.append(first_idx)
            answer.append(second_idx)

        elif len(list_plays) == 1:
            first_idx = list_plays[0][1]
            answer.append(first_idx)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
answer = solution(genres, plays)
print(answer)

