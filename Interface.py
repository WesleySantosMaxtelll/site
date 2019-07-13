
import os, sys
import threading

from Model import Predicter
# from DB_access import AcessaBD

# label = 'pena'

# m = Predicter()
# print(m.predict_text_stance(label, texto))

class interface:
    def __init__(self):
        self.p = Predicter.instance()
        self.dict = {1:'Contrária', 2:'Favorável'}

    def request(self, text, tag):
        d = self.dict[self.p.predict_text_stance(tag, text)]
        print(d)
        return d
