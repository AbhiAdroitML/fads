import os
import scipy
import pandas as pd
import joblib
import pickle

from sentence_transformers import SentenceTransformer

#model = SentenceTransformer('distilbert-base-nli-mean-tokens')
model = SentenceTransformer('bert-base-nli-mean-tokens')

df = pd.read_pickle('07212022_All_Processed_Comments.pkl')
# df = df_comments[df_comments.video_link =='World Star']

# Encoding
sentences = df['comment'].values.tolist()
sentence_embeddings = model.encode(sentences)
print('Sample BERT embedding vector - length', len(sentence_embeddings[0]))

with open('sentence_embeddings_base.pickle', 'wb') as pkl:
    pickle.dump(sentence_embeddings, pkl)
