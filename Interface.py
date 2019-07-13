
import os, sys
import threading

from Model import Predicter
# from DB_access import AcessaBD

# label = 'pena'

# m = Predicter()
# print(m.predict_text_stance(label, texto))

class interface:
    def __init__(self):
        # Novas mensagens
        self.sem_income = threading.Semaphore()
        self.sem_outcome = threading.Semaphore()
        self.list_income = []
        self.list_outcome = []
        self.p = Predicter()
        self.dict = {1:'Contrária', 2:'Favorável'}

    def request(self, text, tag):
        d = self.dict[self.p.predict_text_stance(tag, text)]
        print(d)
        return d
