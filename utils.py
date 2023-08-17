from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import fbeta_score, precision_score, recall_score
import logging


def predict(X_test, model):
    try:
        predictions = model.predict(X_test)
        return predictions
    except Exception:
        logging.info('Error')


def model(X, y):
    try:
        model = RandomForestClassifier()
        smote = SMOTE(random_state=0)
        X_train, y_train = smote.fit_resample(X, y)
        model.fit(X_train, y_train)
        logging.info('SUCCESS!:Model trained and saved')
        return model
    except Exception:
        logging.info('ERROR!:Model not trained and not saved')

def metrics(y, preds):
    try:
        fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
        precision = precision_score(y, preds, zero_division=1)
        recall = recall_score(y, preds, zero_division=1)
        return precision, recall, fbeta
    except Exception:
        logging.info('Error')


def inference(model, X):
    preds = model.predict(X)
    return preds