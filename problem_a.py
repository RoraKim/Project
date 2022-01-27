import json
from pprint import pprint

def movie_info(movie):
    new_dict= {}

    result = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    for key, val in movie.items():
    
        if key in result:
        	new_dict[key] = val
    return new_dict





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))