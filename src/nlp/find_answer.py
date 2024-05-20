import sqlite3 as sql
import nltk
import pymorphy3
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from src.database.db_model import db

def find_answer(text):
    # Вводим список знаков, которые игнорируем
    punctuation_marks = ['!', ',', '(', ')', ':', '-', '?', '.', '..', '...']

    # Подключаем Анализатор морфологичекий
    morph = pymorphy3.MorphAnalyzer()

    # ПОдгружаем справочник стоп слов
    nltk.download('stopwords')
    stop_words = stopwords.words('russian')

    def preprocess(text_message, stop_words_list, punctuation_marks_list, morph_list):
        tokens = word_tokenize(text_message.lower())
        preprocess_text = []
        for token in tokens:
            if token not in punctuation_marks_list:
                lemma = morph_list.parse(token)[0].normal_form
                if lemma not in stop_words_list:
                    preprocess_text.append(lemma)
        return preprocess_text

    my_question = preprocess(text, stop_words, punctuation_marks, morph)

    # db = "sqlite3.db"
    con = sql.connect(db)
    cur = con.cursor()
    cur.execute("select id,key_words from questions;")
    data = cur.fetchall()
    final_data = []
    for i in data:
        my_preprocess = preprocess(str(i[1]), punctuation_marks, stop_words, morph)
        my_preprocess.insert(0, str(i[0]))
        final_data.append(my_preprocess)
    print(final_data)
    checker = {}
    # Нужно переписать.
    for question_base in enumerate(final_data):
        counter = 0

        for word in final_data[question_base[0]]:
            if word in my_question:
                counter = counter + 1
            checker[f'{question_base[1][0]}'] = counter

    answer_id = max(checker, key=checker.get)
    print(answer_id)
    con = sql.connect(db)
    cur = con.cursor()
    cur.execute(f"select answer from questions where id in ({answer_id});")
    result = cur.fetchall()
    print(result[0][0])
    return result[0][0]


if __name__ == "__main__":
    print(find_answer("Каким образом я могу получить доступ к онлайн-платформе для обучения?	"))
