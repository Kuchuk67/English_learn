from voice import voice
from data.d1_1 import data_words_1_1   # сокращенный 1
from data.d1 import data_words_1 # 103 слов
from data.d2 import data_words_2 #  39 слов
from data.d3 import data_words_3    # 143  слов
from data.d4 import data_words_4    # 135  слов
from data.d5 import data_words_5     # 123  слов
from data.d6 import data_words_6   as data_words   # 34  слов

import random
from bottle import route, run, template, request, view, debug

words_d1 = data_words()
keys_words = list(words_d1.keys())
random.shuffle(keys_words)
#values_words_d1 = list(words_d1.values())
step = 1
right_list = []

@route('/')
def index():
    """ Индексная страница - СТАРТ 
    выбираем словари для обучения
    """
    
    return f'<a href="/d1">Выбрать словарь d1</a><br><a href="/d2">Выбрать словарь d2</a>'






lib='d1'
@route(f'/{lib}')
@route(f'/{lib}/')
@route(f'/{lib}/<id_word>')
@view('template_word')
def word(id_word=-1, lib=lib):

    id_word=int(id_word)
    if id_word < 0:
        id_word = 0
        right_list.clear()
        random.shuffle(keys_words)

    e = request.query.e or '0'
    e = int(e)

    r = request.query.r or ''
    if r != '':
        right_list.append(int(r))

    while True:
        if id_word in right_list:
            id_word += 1
            if id_word>=len(keys_words):
                if len(right_list) >= len(keys_words):
                    return '<a href="./">Закончили</a>'
                else:
                    id_word = 0
                #return '<a href="./">Закончили</a>'
            continue
        else:
            break
    
    # Если номер слова перевышает их количество 
    # возвращаемся на первое
    
    if (id_word>=len(keys_words)):
        id_word=0
    
    word = keys_words[id_word]
    translate = words_d1[word] 

    voice(word)
    answer = []
    answer_is = []
    if (e==1):
        answer.append([translate, F"{id_word+1}"])
    else:
        answer.append([translate, F"{id_word+1}?r={id_word}"])
    answer_is.append(id_word)

    for _ in range(0,4):
        x = random.randint(0, len(keys_words)-1)
        
        while True:
            if x in answer_is:
                x = random.randint(0, len(keys_words)-1)
            else:
                break
        answer.append([words_d1[keys_words[x]], F"{id_word}?e=1"])
        answer_is.append(x)
    random.shuffle(answer)

    return dict(translate=word,
                translate_0_link=F"../{lib}/{answer[0][1]}",
                translate_1_link=F"../{lib}/{answer[1][1]}",
                translate_2_link=F"../{lib}/{answer[2][1]}",
                translate_3_link=F"../{lib}/{answer[3][1]}",
                translate_4_link=F"../{lib}/{answer[4][1]}",
                translate_0=answer[0][0],
                translate_1=answer[1][0],
                translate_2=answer[2][0],
                translate_3=answer[3][0],
                translate_4=answer[4][0],
                translate_lib=lib,
                translate_len=f"{len(right_list)}/{len(keys_words)}"
    )







debug(True)
run(host='localhost', port=8080, debug=True, reloader=True)


'''
words = data_words()
i = 0
for key, value in words.items():
    i += 1
    print(i, end =" ")
    print(key, end=": ")
    voice(key)
    x = input()
    print(value, end= "\n")
    
    x = input()
'''