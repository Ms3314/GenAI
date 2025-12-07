# RAG (Retrieval-Augmented Generation) System

A complete implementation of a RAG system that allows you to upload PDF documents, create embeddings, store them in a vector database, and perform intelligent question-answering based on document content.

## 📋 Overview

This project implements a RAG pipeline that:
- Loads and processes PDF documents
- Splits text into manageable chunks
- Creates vector embeddings using OpenAI's embedding models
- Stores embeddings in Qdrant vector database
- Enables semantic search and retrieval of relevant document sections
- Provides an interactive chat interface for document-based Q&A

## 🚀 Features

- **Document Processing**: Load and parse PDF files
- **Text Chunking**: Smart text splitting with overlap for better context retention
- **Vector Embeddings**: High-quality embeddings using OpenAI's `text-embedding-3-small` model
- **Vector Storage**: Efficient storage and retrieval using Qdrant vector database
- **Semantic Search**: Find relevant document sections based on query similarity
- **Interactive Chat**: Command-line interface for querying documents

## 📁 Project Structure

```
RAG/
├── README.md              # This file
├── docker-compose.yml     # Qdrant database setup
├── example.env           # Environment variables template
├── nodejs.pdf            # Sample PDF document
├── indexing.py           # Document processing and indexing
├── chat.py               # Interactive chat interface
└── main.py               # Legacy main file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- OpenAI API key

### Setup

1. **Clone the repository** (if not already done)
   ```bash
   cd /path/to/genai-cohort/RAG
   ```

2. **Install Python dependencies**
   ```bash
   pip install langchain-community langchain-text-splitters langchain-openai langchain-qdrant qdrant-client python-dotenv pypdf
   ```

3. **Set up environment variables**
   ```bash
   cp example.env .env
   ```
   Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY="your_openai_api_key_here"
   HUGGING_FACE="your_hugging_face_token" # Optional
   GROQ_API_KEY="your_groq_api_key"       # Optional
   SEARCH_API_KEY="your_search_api_key"   # Optional
   ```

4. **Start Qdrant vector database**
   ```bash
   docker-compose up -d
   ```

   Verify Qdrant is running:
   ```bash
   curl http://localhost:6333/collections
   ```

## 🔧 Usage

### Step 1: Index Your Documents

Run the indexing script to process and store your PDF documents:

```bash
python indexing.py
```

This will:
- Load the `nodejs.pdf` file
- Split it into chunks of 1000 characters with 200-character overlap
- Create embeddings using OpenAI's model
- Store them in Qdrant with collection name "new-store"

### Step 2: Chat with Your Documents

Start the interactive chat interface:

```bash
python chat.py
```

Example queries:
- "What is Node.js?"
- "How do you create a server in Node.js?"
- "Explain event loops"
- Type "exit" to quit

## 📊 Configuration

### Document Processing Settings

In `indexing.py`, you can modify:

```python
# Text splitting configuration
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Size of each chunk
    chunk_overlap=200     # Overlap between chunks
)

# Embedding model configuration
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=1536       # Embedding dimensions
)
```

### Vector Database Settings

```python
# Collection configuration
vectors_config=VectorParams(
    size=1536,              # Must match embedding dimensions
    distance=Distance.COSINE # Distance metric for similarity
)
```

## 🔍 How It Works

1. **Document Loading**: PDFs are loaded using LangChain's `PyPDFLoader`
2. **Text Chunking**: Documents are split into overlapping chunks for better context
3. **Embedding Creation**: Each chunk is converted to a 1536-dimensional vector using OpenAI's embedding model
4. **Vector Storage**: Embeddings are stored in Qdrant with metadata (page numbers, source)
5. **Similarity Search**: User queries are embedded and compared against stored vectors
6. **Result Retrieval**: Most similar document chunks are returned with context

## 🛡️ Error Handling

The system includes comprehensive error handling:
- Automatic collection creation/recreation if needed
- Graceful handling of PDF parsing issues
- Connection error management for Qdrant
- Detailed error messages and logging

## 🎯 Advanced Features

### Custom PDF Processing
To process different PDF files, modify `indexing.py`:

```python
pdf_path = Path(__file__).parent / "your_document.pdf"
```

### Collection Management
Different document types can use separate collections:

```python
collection_name="your-custom-collection"
```

### Search Parameters
Adjust search results in `chat.py`:

```python
search_results = vector_db.similarity_search(
    query=query,
    k=5  # Number of results to return
)
```

## 🐳 Docker Services

The `docker-compose.yml` provides:
- **Qdrant**: Vector database running on port 6333
- Persistent storage for embeddings
- RESTful API for vector operations

## 📈 Performance Tips

1. **Chunk Size**: Smaller chunks (500-1000 chars) for precise answers, larger chunks (1500-2000) for more context
2. **Overlap**: 10-20% overlap prevents context loss at chunk boundaries
3. **Embedding Model**: `text-embedding-3-small` offers good balance of quality and speed
4. **Batch Processing**: For large documents, consider batch processing embeddings

## 🔧 Troubleshooting

### Common Issues

1. **Qdrant Connection Error**
   ```bash
   # Restart Qdrant
   docker-compose down && docker-compose up -d
   ```

2. **OpenAI API Errors**
   - Check your API key in `.env`
   - Verify you have sufficient credits

3. **PDF Loading Issues**
   - Ensure PDF is not corrupted
   - Check file permissions

4. **Collection Already Exists**
   - The system automatically handles existing collections
   - Check Qdrant logs: `docker-compose logs vector-db`

## 📚 Dependencies

```
langchain-community      # Document loaders
langchain-text-splitters # Text processing
langchain-openai        # OpenAI integration
langchain-qdrant        # Qdrant vector store
qdrant-client          # Qdrant Python client
python-dotenv          # Environment variables
pypdf                  # PDF processing
```

## 🚀 Next Steps

- Add support for multiple file formats (Word, txt, etc.)
- Implement conversation memory for multi-turn chat
- Add web interface using Streamlit or Gradio
- Implement hybrid search (keyword + semantic)
- Add document summarization capabilities

## 📄 License

This project is part of the GenAI Cohort learning materials.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!
