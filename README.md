This code implements a question-answering chatbot using OpenAI's API and Streamlit for a user-friendly interface.
Features:
Document Processing and Embedding: Reads documents from a specified directory (documents/) and creates vector embeddings for efficient search.
Pinecone Vector Search: Utilizes Pinecone as a vector database to store document embeddings and retrieve relevant documents based on user queries.
Question Answering: Leverages a question-answering chain powered by OpenAI's GPT-3.5 turbo model to extract answers from retrieved documents.
Streamlit UI: Provides a web interface with a title, text input box for user queries, and styled answer display area.
Optional Google Search: Includes a checkbox that allows users to choose between using the chatbot (answering from stored documents) or querying Google Search via GPT-3.5 turbo.
Requirements:
Python 3.6 or later
OpenAI API key (set environment variable OPENAI_API_KEY)
Pinecone API key (set environment variable PINECONE_API_KEY)
langchain library
pinecone library
streamlit library
dotenv library (for loading environment variables)
Installation:
Create a virtual environment (recommended).
Install required libraries:
Bash
pip install langchain pinecone streamlit dotenv
Use code with caution.
content_copy
Setup:
Create a directory named documents/ to store your documents (PDFs in this example).
Obtain API keys for OpenAI and Pinecone and set them as environment variables using a .env file or directly in your code.
Running the Code:
Save the code as app.py.
Open a terminal in the project directory and run:
Bash
streamlit run app.py
Use code with caution.
content_copy
Using the Chatbot:
A web interface will launch in your default browser.
Enter your question in the text input box and press Enter.
If the "Use Chatbot" checkbox is selected (default), the chatbot will retrieve answers from stored documents. Otherwise, it will use GPT-3.5 turbo to search the web.
The answer will be displayed with a light blue background and styled text box.
Customization:
Modify the documents/ directory path to store your desired documents.
Adjust styling properties in the CSS code injected through st.write for a different UI appearance.
Explore the langchain and streamlit libraries for further customization options.
Additional Notes:
This code utilizes a simplified document processing approach (reading PDFs). Consider more advanced techniques for complex document structures.
The Google Search functionality via GPT-3.5 turbo provides an alternative information source but might not always be as accurate or relevant as answers retrieved from your stored documents.
