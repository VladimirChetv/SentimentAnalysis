import joblib


class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("./sentement_classifier.pkl")
        self.classes_dict = {0: "Негативный отзыв", 1: "Позитивный отзыв", -1: "Ошибка предсказания"}

    def predict_text(self, text):
        try:
            lst = []
            lst.append(text)
            return self.model.predict(lst)

        except:
            print("Ошибка предсказания")
            return -1

    def predict_list(self, list_of_texts):
        try:

            return self.model.predict(list_of_texts)

        except:
            print('Ошибка предсказания')
            return None

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        class_prediction = prediction[0]
        return self.classes_dict[class_prediction]
