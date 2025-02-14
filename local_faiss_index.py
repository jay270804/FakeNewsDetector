import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# model = SentenceTransformer('sentence-transformers/distilbert-base-nli-mean-tokens')

real_df = pd.read_csv('data/Real_df_for_RAFC.csv')
# Load dataset (example: LIAR)
def create_local_index():
    claims = real_df['title'].tolist()

    # Generate embeddings
    embeddings = model.encode(claims)
    dim = embeddings.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

# Save index
    faiss.write_index(index, "data/local_real_claims.index")

def read_index(claim:str, df:pd.DataFrame , threshold:float = 0.8):
    # local_index = faiss.read_index("data/local_real_claims.index")
    local_index = faiss.read_index("data/local_real_claims_bert.index")
    claim_embed = model.encode([claim])
    D, I = local_index.search(claim_embed, k=3)

    simliar_index = I[0].tolist()
    print(df.iloc[simliar_index])
    # if D[0][0] < threshold:  # Good local match
        # return {"source": "local","threshold": D[0][0], "results": I[0]}
    return {"source": "local","threshold": D[0][0], "results": I[0]}

# create_local_index()
# response = read_index(claim="the unemployment rate for college graduates is 4.4 percent", df=real_df)
# response = read_index(claim="there is growth in federal deficit", df=real_df)
# print(response)
# create_local_index() 