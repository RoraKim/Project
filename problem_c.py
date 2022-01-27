import json
from pprint import pprint


def movie_info(movies, genres):
    movie_info = {'genre_ids' : None,
              'id' : None,
              'overview' : None,
              'poster_path' : None,
              'title' : None,
              'vote_average' : None,
                    }
    for key, value in movie_info.items():
        movie_info[key] = movies[key]

    #비어있는 리스트를 생성한다.
    genre_names =[]
    for i in movie_info['genre_ids']:
        for genre in genres:
            if genre['id'] == i:
                genre_names.append(genre['name'])

    movie_info['genre_names'] = genre_names
    del movie_info['genre_ids']

    

    return movie_info
 
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))