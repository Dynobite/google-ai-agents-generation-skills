## Mine user corrections as labeled failure data.

Every 'no, not like that' from the user is a labeled failure example, and vibe coding produces these in volume. Cluster them and the systematic gaps in the agent become visible, much faster than building a synthetic failure benchmark.

```
Python from google import genai from sklearn.cluster import KMeans client = genai.Client(vertexai=True, project="...", location="...") corrections = [t.user_message for trace in traces for t in trace.turns if t.is_correction] emb = client.models.embed_content( model="text-embedding-005", contents=corrections, ) vectors = [e.values for e in emb.embeddings] clusters = KMeans(n_clusters=8).fit(vectors) # Clusters.labels_ is the prioritized list of failure modes for the next iteration
```

Snippet 4: Clustering user corrections into prioritized failure mode categories.
