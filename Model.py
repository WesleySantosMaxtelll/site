from joblib import dump, load
from Singleton import Singleton
import gc

@Singleton
class Predicter:
    def __init__(self):
        self.initial_path = './modelos/'
        # '/home/maxtelll/Documents/arquivos/site/modelos/'
        # './modelos/'
       

        self.switch_tools_polaridade = {
            'armas': ["polaridade/armas_classifier.joblib", "polaridade/armas_r.joblib"],
            'aborto': ["polaridade/aborto_classifier.joblib", "polaridade/aborto_r.joblib"],
            'cotas': ["polaridade/cotas_classifier.joblib", "polaridade/cotas_r.joblib"],
            'maconha': ["polaridade/maconha_classifier.joblib", "polaridade/maconha_r.joblib"],
            'maioridade': ["polaridade/maioridade_classifier.joblib", "polaridade/maioridade_r.joblib"],
            'pena': ["polaridade/pena_classifier.joblib", "polaridade/pena_r.joblib"]
        }


        self.switch_tools_posicionamento = {
            'armas': ["posicionamento/armas_classifier.joblib", "posicionamento/armas_r.joblib"],
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
        cls_posicionamento, rpt_posicionamento = self._get_tools_posicionamento(label)
        text_vectorized = self.get_text_vectorized(text, rpt_posicionamento)
        gc.collect()
        pred_posicionamento = self.get_predict(text_vectorized, cls_posicionamento)
        gc.collect()
        # print(pred)
        # if pred[0][0] > 3*pred[0][1]:
        #     return 0, 0

        cls_polaridade, rpt_polaridade = self._get_tools_polaridade(label)
        text_vectorized = self.get_text_vectorized(text, rpt_polaridade)
        gc.collect()
        pred_polaridade = self.get_predict(text_vectorized, cls_polaridade)
        gc.collect()

        print(pred_polaridade)
        print(pred_posicionamento)
        # print(pred)
        # if pred[0][0] > pred[0][1]:
        #     return 1, 1
        # else:

        if abs(pred_polaridade[0][0] - pred_polaridade[0][1]) > 0.6:

            if pred_polaridade[0][0] > pred_polaridade[0][1]:
                return 1, 1
            else:
                return 1, 2


        if pred_posicionamento[0][0] > pred_posicionamento[0][1]:
            return 0, 0

        if pred_polaridade[0][0] > pred_polaridade[0][1]:
            return 1, 1
        else:
            return 1, 2