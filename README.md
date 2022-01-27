# 2022_01_21 관통PJT 01

학습 목표

1. 나의 힘으로 문제를 해결해보자. 
2. 그렇다고 모르는걸 고집피우며 아는 척 가만히 있지도 말자.
3. 추후에 참고할 수 있도록 README를 효과적으로 작성해보자. 

-----

### Problem a

접근방향 

먼저 movie가 어떤 형식의 데이터로 주어졌는지 확인하기 위해 print(movie) 또는 import pprint를 이용해 ppritn(movie)를 해준다. 

``` python
{'adult': False, 
 
 vote_average': 8.7, 'vote_count': 18040}
```

딕셔너리 형식임을 알 수 있었다. 

문제에서 주어진 것을 읽어보자

**제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져옵니다.**

라고 한다. 즉, 현재 주어진 데이터에서 필요 없는 값들을 제외하고, 필요한 key, value로 이루어진 새로운 dictionary를 찾아 반환하라는게 문제의 요지이다. 

``` python
def movie_info(movie):
    new_dict = {문제에서 요구하는 key, value로 이루어진 딕셔너리 }
    return new_dict
```

대략적인 틀을 짜면 이렇게 된다. 이렇게 하나하나 나눠서 쉽게 만든다음, 문제에서 요구하는 key와 value값을 넣어줬다. 

#### Q1. Sol1

``` python
def movie_info(movie):
    print(movie)
    new_dict = {
'id' : movie['id'],
'title' : movie['title'],
'poster_path' : movie['poster_path'],
'vote_average' : movie['vote_average'],
'overview' : movie['overview'],
'genre ids' : movie['id']
                    }

    return new_dict
```

문제해결이다. 그런데, 다른 접근 방법은 없을까? 이건 키 값이 많고 복잡해질수록, 실수를 하기 쉬운 방법인 것 같다. 

#### Q1. Sol2

``` python
#최종반환할 딕셔너리
new_dict= {}
#내가 쓸 키 값들을 모아놓은 리스트
result = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
```

movie의 값을 전부 순회할 건데, 나는 key와 value값이 모두 필요하다. new_dict에서 요구하는 값이 key, value모두이기 때문이다. dictionary에서 value값까지 가져오는 방법은? dictionary.items() 이다. 

``` python
new_dict= {}

result = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

for key, val in movie.items():
    print(key, val)
```

``` python
#값
popularity 67.931
poster_path /3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg
release_date 1995-01-28
title 쇼생크 탈출
video False
vote_average 8.7
vote_count 18040
```

print로 어떤 형식으로 반환되는지 확인해줬다. 앞에는 key, 뒤에는 value값이 위치한 것을 볼 수 있다. 

**그렇다면 순회하고 있는 key과 일치하는 값을 result에서 찾은다음, 그 key에 해당하는 key와 value를 모두 new_dict에 추가하여 그 값을 반환하면 된다. **

두번째 솔루션의 로직이 나온 셈이다. 

``` python
def movie_info(movie):
    new_dict= {}

    result = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    for key, val in movie.items():
    
        if key in result:
        	new_dict[key] = val
        
    return new_dict
```

dictionary에 값 넣는 방법

``` python
딕셔너리[키] = 값  
new_dict[key] = val
```



#### 놓친 점 

solution을 한가지 낸것에 빠져 다른 방법도 더 생각해 보지 못했다. 다음번 프로젝트에는 해답이 나오더라도 더 깊게 생각해서 보다 효율적인 방법은 없는지 고민해보겠다. 



#### 아쉬운 점 

지레 겁먹지 않고 하나하나 뜯어서 친근하게 만든다음 적용해봤다면 평소에 풀던 예제 딕셔너리 문제와 아무것도 다를 게 없음을 알 수 있었을 텐데, 첫 관통프로젝트이고 같은 조원들에게 폐를 끼치고 있는것 같다는 생각에 더 소극적이 되었던 것 같다. 

1번문제는 결국

``` python
def movie_info(movie):
    new_dict = {문제에서 요구하는 key, value로 이루어진 딕셔너리 }
    return new_dict
```

이렇게 작은 단위, 내가 이해할 수 있는 단위로 문제를 쪼개 놓고 다시 접근하니 전혀 겁먹을것이 없었다. 다음번 관통 프로젝트에서는 **지레 겁먹지 말자.**



#### 깨달은 점 

막연하게 다 이해했겠지 하고 넘어갔던 개념 중 딕셔너리에 대한 부분이 아직 이해가 덜 되어있다는 것을 이 문제를 풀며 깨달았다. 딕셔너리에 있는 키와 값을 불러오는 방법이나, 값을 추가하는 방법이 미숙했다. 특히, list에만 있는 메소드인 append가 딕셔너리에도 적용되는 줄 알았던 점에서 이해가 부족했다는 것을 느꼈다. 그래서 파이썬 자습서를 다시 읽고, 필요한 정보를 찾아보는 노력을 했다. 시간은 조금 걸렸지만 이해한 줄 알고 넘어갔던 부분을 다시 되짚어 볼 수 있었다. 

-----

### Problem b

**이전단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함수를 완 성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다. **

문제를 처음 봤을 때는 

{ 기존 키 : 값 }의 구조로 된 딕셔너리를 {새로운 키 : 값}의 구조로 바꾸라는 말인가..? 라고 생각했다. 그냥 genre_ids 키를 삭제하고 genre_names 키를 넣으면 안되나? 했다. 그런데 왜 그렇게 해야하는거지..? 라는 의문이 남았다. 



내가 문제를 잘 이해할 수 없었던 이유를 알았다. 같은 조원분들이 계속 pprint로 값을 찍어보고 어떤 type으로 이루어져 있는지를 확인하라고 하셨는데, 어떤 값을 찍어봐야하는지 모르겠었다. 그래서 내가 다루고 있는 데이터가 어떤 형태인지도 모르는 채로 문제를 접근하려 했던 것이다. 

``` python
def movie_info(movie, genres):
    
  print(type(genres))  
```

```python
#값
[{'id': 28, 'name': 'Action'},
 
  {'id': 37, 'name': 'Western'}]
```

눈으로 봐도, type을 찍어봐도 list형태임을 알 수 있다. 너무 긴장하면 할 수 있는 것도 할 수 없다고 생각하게 되는 것 같다. 

출력된 값을 보면 리스트 형식이며, 내용은 id와 name 이라는 키로 이루어져 있는 것을 볼 수 있다. 

그렇다. 문제에서 요구한 것은 **값은 고정시킨 채 키의 이름만 단순히 변경하라는 것이 아닌, Problem A에서 구한 값 중 id 가 가진 값을 토대로, 그 값이 의미하는 name을 찾아오라는 의미였던 것이다. **



우선, problem a에서 도출한 결과를 응용하여, id를 제외한 키, 값을 가진 딕셔너리를 생성한다.

``` python
   new_dict = {}
    result = ['id', 'title', 'poster_path', 'vote_average', 'overview']
    for key, val in movie.items():
        if key in result:
            new_dict[key] = val
```

여기에 새로운 name 키를 가진 딕셔너리를 추가해주면 된다. 

어떻게 만들까? 먼저 다른 변수에 ids를 따로 담아보자. 

``` python
# movie가 가지고 있는 genre_ids
ids = movie['genre_ids'] # -> [18, 20 ...]
```

장르 정보를 순회하면서 딕셔너리 하나가 가지고 있는 키 id에 해당하는 value가 내가 가지고 있는 ids 리스트에 있는지 확인하기 

``` python
 # 이름만 모아놓은 리스트
    names = []

    # 장르 전체 순회
    for genre in genres:
        # genre에 뭐 들어있는지 확인
        # print(genre) # -> {'id': 28, 'name': 'Action'}
        # 만약에 genre['id']가 ids 에 들어 있다면
        if genre['id'] in ids:
            # 내가 찾는 장르 name을 가지고 있는 딕셔너리를 찾았다.
            # 근데 이름들만 모아 놓을 건데... 생각해보니까 이름들은 리스트로 넣어야 한다.
            # 위로 돌아가서 이름들만 모아 놓은 리스트를 만들자.
            # 위에서 만든 names 리스트에 지금 순회중인 genre가 가지고 있는 name을 추가하자.
            
            # 리스트에 값 추가하기
            # 1. append
            # names.append(genre['name])
            
            # 2. list + list
            # 내가 필요한건 이 딕셔너리가 가지고 있는 name만 있으면 된다.
            # 장르 이름을 리스트 [] 로 감싸서 리스트 + 리스트 가능하게 하기
            names += [genre['name']]
        # 위 작업을 장르 전체를 다 순회 할때까지 반복
        # ids에 어떤 id가 있을지 모르니까 전부 순회하는 것
    
    # 순회가 다 끝났다 -> names에 내가 필요한 장르 이름들이 다 들어갔다
    # 확인
    # print(names)
    
    # 자 그럼 최종 제출해야 하는 답은 이 장르 이름 목록을 가진 딕셔너리다.
    # 위에서 만든 new_dict에는 아직 'genre_names' 키와 value가 없다. 집어 넣자.
    new_dict['genre_names'] = names

```



### Problem c

### Problem d

### Problem e

