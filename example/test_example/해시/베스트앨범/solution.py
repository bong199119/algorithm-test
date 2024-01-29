def sort_genres(dict_genres):
    list_genre = []
    return list_genre

def sort_plays(list_plays):
    return list_plays

def solution(genres, plays):
    answer = []
    dict_genres = {}

    for idx, play in enumerate(plays):
        if genres[idx] not in dict_genres:
            dict_genres[genres[idx]] = {}
            dict_genres[genres[idx]]['plays'] = [[play, idx]]
            dict_genres[genres[idx]]['total plays'] = play

        else:
            dict_genres[genres[idx]]['plays'].append([play, idx])
            dict_genres[genres[idx]]['total plays'] += play

    list_genre = sort_genres(dict_genres)

    for genre in list_genre:
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

