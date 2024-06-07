from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import networkx as nx

def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words and word.isalnum()]
    
    return words

def calculate_word_frequencies(words):
    # Calculate word frequencies
    word_freq = FreqDist(words)
    return word_freq

def extractive_summarization(text, num_sentences=3):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    
    # Preprocess sentences and join back into strings
    preprocessed_sentences = [' '.join(preprocess_text(sentence)) for sentence in sentences]
    
    # Calculate TF-IDF matrix
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_sentences)
    
    # Calculate cosine similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Create graph representation of sentences
    sentence_graph = nx.from_numpy_array(similarity_matrix)
    
    # Calculate PageRank scores for sentences
    sentence_scores = nx.pagerank(sentence_graph)
    
    # Sort sentences by PageRank score
    ranked_sentences = sorted(((score, idx) for idx, score in sentence_scores.items()), reverse=True)
    
    # Get top scoring sentences
    top_sentence_indices = [idx for _, idx in ranked_sentences[:num_sentences]]
    
    # Generate summary
    summary = ' '.join([sentences[i] for i in sorted(top_sentence_indices)])
    
    return summary