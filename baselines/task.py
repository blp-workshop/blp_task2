import pandas as pd
import random
import logging
import argparse
from os.path import join, dirname, basename
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import csv

import sys
sys.path.append('.')

from scorer.task2 import evaluate
from format_checker.task2 import check_format

random.seed(0)
ROOT_DIR = dirname(dirname(__file__))

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

def run_majority_baseline(data_fpath, test_fpath, results_fpath):
    train_df = pd.read_csv(data_fpath, dtype=object, encoding="utf-8", sep='\t')
    test_df = pd.read_csv(test_fpath, dtype=object, encoding="utf-8", sep='\t')

    pipeline = DummyClassifier(strategy="most_frequent")

    text_head = "text"
    id_head = "id"

    pipeline.fit(train_df[text_head], train_df['label'])

    with open(results_fpath, "w") as results_file:
        predicted_distance = pipeline.predict(test_df[text_head])

        results_file.write("id\tlabel\n")

        for i, line in test_df.iterrows():
            label = predicted_distance[i]

            results_file.write("{}\t{}\n".format(line[id_head], label))


def run_random_baseline(data_fpath, results_fpath):
    gold_df = pd.read_csv(data_fpath,  dtype=object, encoding="utf-8", sep='\t')
    #label_list=gold_df['label'].to_list()
    label_list = ["Positive", "Negative", "Neutral"]


    id_head = "id"

    with open(results_fpath, "w") as results_file:
        results_file.write("id\tlabel\n")
        for i, line in gold_df.iterrows():
            results_file.write('{}\t{}\n'.format(line[id_head],random.choice(label_list)))


def run_ngram_baseline(train_fpath, test_fpath, results_fpath):
    train_df = pd.read_csv(train_fpath, dtype=object, encoding="utf-8", sep='\t')
    test_df = pd.read_csv(test_fpath, dtype=object, encoding="utf-8", sep='\t')

    text_head = "text"
    id_head = "id"

    pipeline = Pipeline([
        ('ngrams', TfidfVectorizer(ngram_range=(1, 1),lowercase=True,use_idf=True,max_df=0.95, min_df=3,max_features=5000)),
        ('clf', SVC(C=1, gamma='scale', kernel='linear', random_state=0))
    ])
    pipeline.fit(train_df[text_head], train_df['label'])

    with open(results_fpath, "w") as results_file:
        predicted_distance = pipeline.predict(test_df[text_head])
        results_file.write("id\tlabel\n")
        for i, line in test_df.iterrows():
            label = predicted_distance[i]
            results_file.write("{}\t{}\n".format(line[id_head], label))


def run_baselines(train_fpath, test_fpath):
    majority_baseline_fpath = join(ROOT_DIR,
                                 f'data/majority_baseline_{basename(test_fpath)}')
    run_majority_baseline(train_fpath, test_fpath, majority_baseline_fpath)

    if check_format(majority_baseline_fpath):
        acc, precision, recall, f1 = evaluate(majority_baseline_fpath, test_fpath)
        logging.info(f"Majority Baseline F1-micro: {f1}")


    random_baseline_fpath = join(ROOT_DIR, f'data/random_baseline_{basename(test_fpath)}')
    run_random_baseline(test_fpath, random_baseline_fpath)

    if check_format(random_baseline_fpath):
        acc, precision, recall, f1 = evaluate(random_baseline_fpath, test_fpath)
        logging.info(f"Random Baseline F1-micro: {f1}")

    ngram_baseline_fpath = join(ROOT_DIR, f'data/ngram_baseline_{basename(test_fpath)}')
    run_ngram_baseline(train_fpath, test_fpath, ngram_baseline_fpath)
    if check_format(ngram_baseline_fpath):
        acc, precision, recall, f1 = evaluate(ngram_baseline_fpath, test_fpath)
        logging.info(f"Ngram Baseline F1-micro: {f1}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-file-path", "-t", required=True, type=str,
                        help="The absolute path to the training data")
    parser.add_argument("--dev-file-path", "-d", required=True, type=str,
                        help="The absolute path to the dev data")
    #parser.add_argument("--lang", "-l", required=True, type=str,
    #                    choices=['arabic', 'english', 'spanish'],
    #                    help="The language of the subtask")

    args = parser.parse_args()
    run_baselines(args.train_file_path, args.dev_file_path)


    #python -t /home/bjit/Nandi-AI/NLP/clef2022-checkthat-lab/task1/data/subtasks-english/CT22_english_1B_claim/CT22_english_1B_claim_train.tsv -d /home/bjit/Nandi-AI/NLP/clef2022-checkthat-lab/task1/data/subtasks-english/CT22_english_1B_claim/CT22_english_1B_claim_dev.tsv -l english
