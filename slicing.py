from dataprocessing import dataprocessing
from clean import get_data, data_cleaning
from utils import model, \
    metrics, predict
from joblib import dump
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(
    filename='./logging',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

def split(data):
    try:
        train, test = train_test_split(data, test_size=0.30, random_state=0)
        return train, test
    except Exception:
        logging.info('error')


def slicing(data):
    sliced = []

    for category in cat_features:
        for cls in test[category].unique():
            df_temp = test[test[category] == cls]
            X_test_temp, y_test_temp, _, _ = dataprocessing(
                df_temp, categorical_features=cat_features,
                label="salary", encoder=encoder, lb=lb, training=False)
            y_preds = model.predict(X_test_temp)
            precision_temp, recall_temp, fbeta_temp = metrics(
                y_test_temp, y_preds)
            results = "[%s->%s] Precision: %s " \
                "Recall: %s FBeta: %s" % (
                    category,
                    cls,
                    precision_temp,
                    recall_temp,
                    fbeta_temp)
            sliced.append(results)

    with open('slice_output.txt', 'w') as out:
        for slice in sliced:
            out.write(slice + '\n')


if __name__ == '__main__':
    df = get_data('clean_census.csv')
    train, test = split(df)
    test.to_csv('output.csv')
    X_train, y_train, encoder, lb = dataprocessing(
        train, categorical_features=cat_features,
        label="salary", training=True)
    X_test, y_test, encoder_t, lb_t = dataprocessing(
        test, categorical_features=cat_features,
        label="salary", training=False, encoder=encoder, lb=lb)
    dump(encoder_t, 'encoder.joblib')
    dump(lb_t, 'lb.joblib')
    model = model(X_train, y_train)
    dump(model, 'model.joblib')
    predictions = predict(X_test, model)
    precision, recall, fbeta = metrics(y_test, predictions)
    slicing(df)