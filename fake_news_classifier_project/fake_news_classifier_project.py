import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#Evaluate model performance.
from sklearn import metrics

import matplotlib.pyplot as plt
import numpy as np
import itertools

def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):
    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()

#import the fake news .csv
df = pd.read_csv("C:\\Users\\pheli\\Documents\\fake_or_real_news.csv")

#prints the shape of the dataframe
df.shape

#changing column names...
df.columns = ['id', 'title', 'text', 'label']
#set the index of the dataframe
df = df.set_index("id")
#sorting by the first column...
df = df.sort_values(by=['id'])
#prints the first lines of the dataframe
df.head()

y = df.label

#getting the training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size =0.33, random_state=53)

#count_vectorizer will turn texts into a bag-of-words vector.
#as a preprocessing step, the stop word will be removing(such as 'a', 'about', 'an', 'and', 'any', 'do' and so on).
count_vectorizer = CountVectorizer(stop_words='english')

#will generate a mapping of words with ids and vectors representing
#how many times each word appears in the news.
#learn the vocabulary dictionary and return term-document matrix.
#X_train.values shows only the texts.
count_train = count_vectorizer.fit_transform(X_train.values)

#transform documents to document-term matrix.
count_test = count_vectorizer.transform(X_test)

print(count_vectorizer.get_feature_names())

print(count_train.toarray())

nb_classifier = MultinomialNB()

nb_classifier.fit(count_train, y_train)

#this will determine the internal parameters based on the dataset.
nb_classifier.fit(count_train, y_train)

#this will use the trained model to predict the label based on the test data vectors.
pred = nb_classifier.predict(count_test)

#to further evaluate our model, we can also check the confusion matrix which shows correct
#and incorrect labels.
cm = metrics.confusion_matrix(y_test, pred, labels=['FAKE', 'REAL'])
plot_confusion_matrix(cm=cm, normalize=False, target_names=['FAKE', 'REAL'], title = 'Confusion Matrix')
