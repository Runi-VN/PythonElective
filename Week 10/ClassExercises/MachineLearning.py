from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import load_digits
corpus = open('moby_dick.txt', 'r', encoding='utf-8').readlines()
vectorizer = CountVectorizer(encoding='utf-8')

fit = vectorizer.fit_transform(corpus)
print(type(fit))
res = fit.todense()  # returns a numpy array of same shape
document_idx = vectorizer.vocabulary_['wood']
# sum all row cells where column == index
document_count = sum(res[:, document_idx])
print('word occurs {} times in the text'.format(document_count))
