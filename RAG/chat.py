from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    # With the `text-embedding-3` class
    # of models, you can specify the size
    # of the embeddings you want returned.
    dimensions=1536
)

vector_db = QdrantVectorStore.from_existing_collection(
    port=6333,
    collection_name="new-store",
    embedding=embedding_model
)

# take the user query 
query = input(">>>")
# vector similarity search in DB 
if (query == "exit"):
    exit 
else:
    search_results = vector_db.similarity_search(
        query=query
    )
    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])
    data = str(context)  # Converts list to string but shows brackets and quotes
    # print(data)
    
    SYSTEM_PROMPT = f"""
    You are a helpfull AI Assistant who asnweres user query based on the available context
    retrieved from a PDF file along with page_contents and page number.

    You should only ans the user based on the following context and navigate the user
    to open the right page number to know more.

    Context:
    {context}
    """
    
    llm = ChatOpenAI(
        model="gpt-5-mini"
    )
    
    message = [
            {"role" : "system" , "content" : SYSTEM_PROMPT},
            {"role" : "user" , "content" : query}    
        ]
    
    print(llm.invoke(message).content)