import json
from pprint import pprint


def movie_info(movie, genres):
    new_dict= {}

    result = ['title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    for key, val in movie.items():
    
        if key in result:
            new_dict[key] = val
    print(new_dict)



    
    






  

    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))