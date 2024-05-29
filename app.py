import openai
import langchain
import pinecone
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st  # Added Streamlit for UI
load_dotenv()
api_key_pinecone = os.getenv("PINECONE_API_KEY")
environment = "us-east-1"

## Lets Read the document
def read_doc(directory):
   file_loader=PyPDFDirectoryLoader(directory)
   documents=file_loader.load()
   return documents
doc=read_doc('documents/')
len(doc)
## Divide the docs into chunks
def chunk_data(docs,chunk_size=1000,chunk_overlap=50):
   text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
   doc=text_splitter.split_documents(docs)
   return docs
documents=chunk_data(docs=doc)
len(documents)
embeddings = OpenAIEmbeddings(api_key=os.environ['OPENAI_API_KEY'])
# Create a Pinecone client instance
pinecone_client = pinecone.Pinecone(api_key_pinecone=api_key_pinecone, environment=environment)
index_name="chatbotpip"
# Index creation (assuming documents and embeddings are ready)
index = Pinecone.from_documents(doc, embeddings, index_name=index_name)

#vectors=embeddings.embed_query("How are you?")
#vectors
## Vector Search DB In Pinecone
api_key_pinecone = os.getenv("PINECONE_API_KEY")
environment = "us-east-1"
# Create a Pinecone client instance
pinecone_client = pinecone.Pinecone(api_key_pinecone=api_key_pinecone, environment=environment)
print(api_key_pinecone)
index_name="chatbotpip"
index=Pinecone.from_documents(doc,embeddings,index_name=index_name)
## Cosine Similarity Retreive Results from VectorDB
def retrieve_query(query,k=2):
   matching_results=index.similarity_search(query,k=k)
   return matching_results
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
llm=OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0.5)
chain=load_qa_chain(llm,chain_type="stuff")
## Search answers from VectorDB
def retrieve_answers(query):
   doc_search=retrieve_query(query)
   response=chain.run(input_documents=doc_search,question=query)
   return response
st.title("Chatbot :) ")
user_query = st.text_input("Ask me anything:")

if user_query:
     answer = retrieve_answers(user_query)
     with st.container():
       st.write(f"<style>.stContainer {{background-color: #e0ffff; padding: 10px;}}</style>", unsafe_allow_html=True)
       st.write(f"<style>.stTextInput {{border: 1px solid #ccc; border-radius: 5px; padding: 5px;}}</style>", unsafe_allow_html=True)
       st.write(answer)
