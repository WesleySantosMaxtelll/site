from joblib import dump, load
from Singleton import Singleton

@Singleton
class Predicter:
    def __init__(self):
        self.initial_path = './modelos/'
        # '/home/maxtelll/Documents/arquivos/site/modelos/'
        # './modelos/'
        

        self.switch_tools_polaridade = {
            'aborto': ["polaridade/aborto_classifier.joblib", "polaridade/aborto_r.joblib"],
            'cotas': ["polaridade/cotas_classifier.joblib", "polaridade/cotas_r.joblib"],
            'maconha': ["polaridade/maconha_classifier.joblib", "polaridade/maconha_r.joblib"],
            'maioridade': ["polaridade/maioridade_classifier.joblib", "polaridade/maioridade_r.joblib"],
            'pena': ["polaridade/pena_classifier.joblib", "polaridade/pena_r.joblib"]
        }


        self.switch_tools_posicionamento = {
            'aborto': ["posicionamento/aborto_classifier.joblib", "posicionamento/aborto_r.joblib"],
            'cotas': ["posicionamento/cotas_classifier.joblib", "posicionamento/cotas_r.joblib"],
            'maconha': ["posicionamento/maconha_classifier.joblib", "posicionamento/maconha_r.joblib"],
            'maioridade': ["posicionamento/maioridade_classifier.joblib", "posicionamento/maioridade_r.joblib"],
            'pena': ["posicionamento/pena_classifier.joblib", "posicionamento/pena_r.joblib"]
        }




    def load_file(self, path):
        return load(self.initial_path + path)

    def _get_tools_posicionamento(self, label):
        classifier, representation = self.switch_tools_posicionamento.get(label, (None, None))
        print(classifier)
        print(representation)
        return classifier, representation

    def _get_tools_polaridade(self, label):
        classifier, representation = self.switch_tools_polaridade.get(label, (None, None))
        print(classifier)
        print(representation)
        return classifier, representation

    def get_text_vectorized(self, text, representation):
        r = self.load_file(representation)
        return r.transform([text])

    def get_predict(self, text_vectorized, classifier):
        c = self.load_file(classifier)
        return c.predict_proba(text_vectorized)

    def predict_text_stance(self, label, text):
        print(text)
        classifier, representation = self._get_tools_posicionamento(label)
        text_vectorized = self.get_text_vectorized(text, representation)
        pred = self.get_predict(text_vectorized, classifier)
        print(pred)
        if pred[0][0] > 3*pred[0][1]:
            return 0, 0

        classifier, representation = self._get_tools_polaridade(label)
        text_vectorized = self.get_text_vectorized(text, representation)
        pred = self.get_predict(text_vectorized, classifier)
        print(pred)
        if pred[0][0] > pred[0][1]:
            return 1, 1
        else:
            return 1, 2

