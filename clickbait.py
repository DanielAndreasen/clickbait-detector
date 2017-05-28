import os
import cPickle
import argparse

def _parser():
    parser = argparse.ArgumentParser(description='Clickbait detector!')
    parser.add_argument('title', help='Article title to detect for clickbait', nargs='+')
    parser.add_argument('-t', '--train', help='Force retraining', action='store_true')
    return parser.parse_args()

def create_classifier():
    # import numpy as np
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.linear_model import SGDClassifier

    ## Create a pipeline
    clf = Pipeline([('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB())])


    ## Getting the data
    with open('dataset/clickbait_data', 'r') as f:
        clickbait = f.readlines()

    with open('dataset/non_clickbait_data', 'r') as f:
        non_clickbait = f.readlines()
    X = clickbait + non_clickbait
    y = [1]*len(clickbait) + [0]*len(non_clickbait)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    clf = clf.fit(X, y)
    # predicted = clf.predict(X_test)
    # print np.mean(predicted == y_test)
    with open(clickbait_classifier, 'wb') as f:
        cPickle.dump(clf, f)
    return clf


if __name__ == '__main__':
    args = _parser()
    clickbait_classifier = 'clickbait.pkl'
    if os.path.isfile(clickbait_classifier):
        with open(clickbait_classifier, 'rb') as f:
            clf = cPickle.load(f)
    elif args.train:
        clf = create_classifier()
    else:
        clf = create_classifier()

    title = args.title[0]
    while True:
        pred = clf.predict([title])
        if pred[0]:
            print 'Clickbait detected! Abort mission!'
        else:
            print 'Safe to read. No neurons will die here!'

        title = raw_input('Title: ')
        if title.lower() == 'q':
            break
