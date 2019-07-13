
from joblib import dump, load


class Predicter:
    def __init__(self):
        self.initial_path = './modelos/'
        # '/home/maxtelll/Documents/arquivos/site/modelos/'
        # './modelos/'
        
        def load_file(path):
            return load(self.initial_path + path)

        self.switch_tools = {
            'aborto': [load_file("aborto_classifier.joblib"), load_file("aborto_r.joblib")],
            'cotas': [load_file("cotas_classifier.joblib"), load_file("cotas_r.joblib")],
            'maconha': [load_file("maconha_classifier.joblib"), load_file("maconha_r.joblib")],
            'maioridade': [load_file("maioridade_classifier.joblib"), load_file("maioridade_r.joblib")],
            'pena': [load_file("pena_classifier.joblib"), load_file("pena_r.joblib")]
        }


    def _get_tools(self, label):
        classifier, representation = self.switch_tools.get(label, (None, None))
        return classifier, representation

    def predict_text_stance(self, label, text):
        print(text)
        classifier, representation = self._get_tools(label)
        # print(representation)
        text_vectorized = representation.transform([text])
        # print(len(text_vectorized.toarray()[0]))
        # print(text_vectorized.toarray())
        pred = classifier.predict(text_vectorized)
        return pred[0]

