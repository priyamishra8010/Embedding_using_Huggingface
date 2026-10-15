# Text Embeddings Using Hugging Face

## Project Overview
This project demonstrates how to convert text documents into numerical vectors using Hugging Face sentence-transformer embeddings and LangChain. These vectors can be used in semantic search, document retrieval, and Retrieval-Augmented Generation (RAG) applications.

## Features
- Converts text into numerical vector representations.
- Uses the `all-MiniLM-L6-v2` sentence-transformer model.
- Generates embeddings for multiple documents.
- Displays the number of generated embeddings and vector dimensions.

## Technologies Used
- Python
- LangChain
- Hugging Face
- Sentence Transformers

## Installation
Install the required libraries:

`pip install langchain-huggingface sentence-transformers`

## How to Run
Run the following command:

`python embeddings.py`

The script generates an embedding vector for each input document and displays the number of vectors and the dimensions of an individual vector.

## Learning Outcome
Learned how text embeddings represent natural language as numerical vectors and how these representations form a foundation for semantic search and RAG applications.
