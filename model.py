import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support

from sklearn.feature_extraction.text import TfidfVectorizer

def get_metrics(mod, X, y):
    """
    This function takes in:
    - mod: model being used
    - X: X_train/validate/test: split features
    - y: target
    
    """
    baseline_accuracy = 0.21626984126984128
    y_pred = mod.predict(X)
    accuracy = mod.score(X, y)
    conf = confusion_matrix(y, y_pred)
    prfs = pd.DataFrame(precision_recall_fscore_support(y, y_pred), index=['precision', 'recall', 'f1-score', 'support'])
    
    print(f'''
    BASELINE accuracy is: {baseline_accuracy:.3%}
    The accuracy for our model is: {accuracy:.3%} 
    ''')
    return prfs





def language_predictor(text):
    """
    This function takes in text from a readme
    - cleans the text
    - creates a Series to hold the text
    - scales the text
    returns the predicted language of the Github repo
    """
    tfidf = TfidfVectorizer()
    readmetext = w.clean(text, extra_words = ['r', 'u', '2', 'ltgt', "'"])

    readme_series = pd.Series([readmetext])
    readme_series = tfidf.transform(readme_series)
    print(knn.predict(readme_series))