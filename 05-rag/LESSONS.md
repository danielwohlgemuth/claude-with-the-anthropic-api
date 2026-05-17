# RAG Lessons
- Chunking Strategies
    - Character-based: reliable as there is no need to understand the text, but may split text in unexpected places
    - Sentence-based: more reliable for plain text than character-based, but less suitable for other formats
    - Section-based: requires understanding the document structure and assumes consistent formatting

- Similarity can be measured with the cosine similarity metric. Values closer to 1 indicate the vectors are more similar and values closer to -1 indicate the vectors are dissimilar. Cosine distance is 1 minus the cosine similarity, so it's just shifted by 1, meaning that similar vectors have values close to 0.

## RAG Pipeline
```mermaid
graph TD
    document(["Document"])
    chunking["Chunking\nSplit document into smaller pieces"]
    chunk(["Chunk"])
    contextualize["Contextualize\nAugment chunk with relevant information from the document"]
    chunk_context(["Chunk + Context"])
    embedding["Embedding\nConvert chunk to vector representation"]
    tf_idf["TF-IDF\nTerm Frequency-Inverse Document Frequency"]
    vector_db(["Vector DB"])
    tf_idf_index(["TF-IDF Index"])
    query(["Query"])
    rank_fusion["Rank Fusion\nCombine chunks from multiple search methods"]
    reranker["Reranker\nReorder the combined chunks by relevance to the query"]
    answer["Answer"]

    document --> chunking
    chunking --> chunk
    chunk --> contextualize
    document --> contextualize
    contextualize --> chunk_context
    chunk_context --> embedding
    chunk_context --> tf_idf
    embedding --> vector_db
    tf_idf --> tf_idf_index

    query --> vector_db
    query --> tf_idf_index
    query --> reranker
    query --> answer
    vector_db --> rank_fusion
    tf_idf_index --> rank_fusion
    rank_fusion --> reranker
    reranker --> answer

    subgraph preprocessing_sg [Preprocessing]
        document
        chunking
        chunk
        contextualize
        chunk_context
        embedding
        tf_idf
    end

    subgraph query_sg [Query]
        query
        rank_fusion
        reranker
        answer
    end

    style preprocessing_sg fill:#E1F5FE
    style query_sg fill:#E8F5E9
```