from voice import voice
from data.d1 import data_words
import random
from bottle import route, run, template, view, debug

words_d1 = data_words()
keys_words_d1 = list(words_d1.keys())
values_words_d1 = list(words_d1.values())
step = 1

@route('/')
def index():
    """ Индексная страница - СТАРТ 
    выбираем словари для обучения
    """
    return '<a href="/d1/world">Выбрать словарь d1</a>'

@route('/hello')
@route('/hello/<name>')
@view('template')
def hello(name='World'):
    return dict(name=name)


@route('/d1/<id_word>')

def word(id_word):
    id_word = int(id_word)

    word = keys_words_d1[id_word]
    translate = values_words_d1[id_word]

    voice(word)
    answer = []
    answer_is = []
    answer.append([translate, id_word+1])
    answer_is.append(id_word)

    for _ in range(0,4):
        x = random.randint(0, len(values_words_d1))
        
        while True:
            if x in answer_is:
                x = random.randint(0, len(values_words_d1))
            else:
                break

        answer.append([values_words_d1[x], id_word])
        answer_is.append(x)


    random.shuffle(answer)
    print(answer)
    #table_answer = f'<a href="/">{}</a>'

    return template('<h1>{{word}}</h1><br /> '
    '<a href="{{translate[0][1]}}" style="text-decoration: none; color: #444;">{{translate[0][0]}}</a><br />' \
    '<a href="{{translate[1][1]}}" style="text-decoration: none; color: #444;">{{translate[1][0]}}</a><br /> ' \
    '<a href="{{translate[2][1]}}" style="text-decoration: none; color: #444;">{{translate[2][0]}}</a><br /> ' \
    '<a href="{{translate[3][1]}}" style="text-decoration: none; color: #444;">{{translate[3][0]}}</a><br /> ' \
    '<a href="{{translate[4][1]}}" style="text-decoration: none; color: #444;">{{translate[4][0]}}</a><br /> ' \
    , word=word, translate=answer)





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