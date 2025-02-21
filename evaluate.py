import argparse

from pysondb import db
from sklearn.metrics import f1_score

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('file', type=str)
    args = parser.parse_args()

    predictions_db = db.getDb(args.file)
    predictions = predictions_db.getAll()

    predicted = []
    labels = []

    for record in predictions:

        if record["label"] == 1 or record["label"] == 0:
            predicted.append(record["prediction"])
            labels.append(record["label"])


    print(f1_score(labels, predicted))
