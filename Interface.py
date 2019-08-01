
import os, sys
import threading

from Model import Predicter
from DB_access import AcessaBD
# from DB_access import AcessaBD

# label = 'pena'

# m = Predicter()
# print(m.predict_text_stance(label, texto))

class interface:
    def __init__(self):
        self.p = Predicter.instance()
        self.db = AcessaBD()
        self.dict = {1:'Contrária', 2:'Favorável'}
        self.dict_p = {'Contrária':"against", 'Favorável':"for", 'Sem Posicionamento':"others"}

    def request(self, text, tag):
        cat, pred = self.p.predict_text_stance(tag, text)
        d = None
        if cat == 0:
            d = 'Sem Posicionamento'
        else:
            d = self.dict[pred]
        print(d)

        # self.db.inserir_texto(text, tag, 'for', 'others')
        return d

    def get_textos(self):
        return self.db.get_textos()

    def save_text(self, text, tag, ans, predicted):
        print(predicted)
        self.db.inserir_texto(text, tag, ans, self.dict_p[predicted])

    def statiscts(self):
        return self.db.get_total(), self.db.get_precisao()