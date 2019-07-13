from joblib import dump, load
from Singleton import Singleton

@Singleton
class Predicter:
    def __init__(self):
        self.initial_path = './modelos/'
        # '/home/maxtelll/Documents/arquivos/site/modelos/'
        # './modelos/'
        

        self.switch_tools = {
            'aborto': ["aborto_classifier.joblib", "aborto_r.joblib"],
            'cotas': ["cotas_classifier.joblib", "cotas_r.joblib"],
            'maconha': ["maconha_classifier.joblib", "maconha_r.joblib"],
            'maioridade': ["maioridade_classifier.joblib", "maioridade_r.joblib"],
            'pena': ["pena_classifier.joblib", "pena_r.joblib"]
        }


    def load_file(self, path):
        return load(self.initial_path + path)

    def _get_tools(self, label):
        classifier, representation = self.switch_tools.get(label, (None, None))
        print(classifier)
        print(representation)
        return classifier, representation

    def get_text_vectorized(self, text, representation):
        r = self.load_file(representation)
        return r.transform([text])

    def get_predict(self, text_vectorized, classifier):
        c = self.load_file(classifier)
        return c.predict(text_vectorized)

    def predict_text_stance(self, label, text):
        print(text)
        classifier, representation = self._get_tools(label)
        text_vectorized = self.get_text_vectorized(text, representation)
        pred = self.get_predict(text_vectorized, classifier)
        return pred[0]

