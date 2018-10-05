import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
from gensim.models.tfidfmodel import TfidfModel

#Creating a Gensim Dictionary

my_documents = ['The movie was about a spaceship and aliens. The aliens were very ugly. The spaceship was amazing!',
                'I really liked the movie!',
                'Awesome actions scenes, but boring characters.',
                'The movie was awful! I hate aliens films.',
                'Space is cool! I liked the movie.',
                'More space films, please!']

#Preprocessing
tokenized_docs = [word_tokenize(doc.lower()) for doc in my_documents]

print(tokenized_docs)

#Will create a map with an id for each token. This is the beggining of the corpus
#Now we can represent whole documents using just a list of their token ids and how often
#those tokens appear in each document.
dictionary = Dictionary(tokenized_docs)
print(dictionary)
print(dictionary.token2id)

#Gensim transform each document into a bag of words using the token ids and the frequency of each token in the
#document. Gensim corpus is a list of lists, each list representing one document.
#The first item represents the token id from the dictionary and the second item represents the token frequency in
#the document.
#This is a little different than normal corpus is usually a collection of documents.
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
print(corpus)

"""
    gensim models can be easily saved, updated, and reused.
    Our dictionary can also be updated.
    This more advanced and feature rich bag-of-words can be use in future exercises.
"""


# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("movie")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in tokenized_docs]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])

# Save the fifth document: doc
doc = corpus[0]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)

#Term frequency - inverse document frequency
tfidf = TfidfModel(corpus)
print(tfidf[corpus[0]])
print(dictionary.get(7))


# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary[term_id], weight)

