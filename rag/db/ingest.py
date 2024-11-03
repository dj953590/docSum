import os
import logging

import rag
from constants import PERSIST_DIRECTORY, SOURCE_DIRECTORY, TMP_DIRECTORY
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from rag.extractor.extractor import ItemExtractor
from rag.db.folders import get_recent_folders

load_dotenv()


def create_DB(symbol):
    db_path = f"{PERSIST_DIRECTORY}/{symbol}/item_7/chroma.sqlite3"
    if os.path.exists(db_path):
        logging.info(f"Vector database already created for {symbol}")
        return ""

    logging.info(f"Loading documents from {SOURCE_DIRECTORY}/{symbol}/10-K/")
    # Path to the symbol's 10-K directory
    dir_path = os.path.join(SOURCE_DIRECTORY, symbol, "10-K")
    recent_folders = get_recent_folders(dir_path, num_years=3)
    # print(recent_folders)
    all_docs = []
    for year_folder in recent_folders:
        year_folder_path = os.path.join(dir_path, year_folder)
        if not os.path.isdir(year_folder_path):
            raise (f"Directory {year_folder_path} does not exist")
        doc_path = os.path.join(year_folder_path, "primary-document.html")
        extractor: ItemExtractor = ItemExtractor(doc_path)

        # Extract the content for Items 1, 1a, 7, 7a and 8
        item_1_1a_text = extractor.extract_item_1_1a_content()
        item_7_7a_text = extractor.extract_item_7_7a_content()
        item_8_text = extractor.extract_item_8_content()
        all_item_text = item_1_1a_text + '\n' + item_7_7a_text + '\n' + item_8_text

        # Save the extracted content to a file
        file_name = f"{symbol}_{year_folder.split('-')[1]}.txt"
        ext_path = os.path.join(TMP_DIRECTORY, file_name)
        rag.extractor.extractor.save_content_to_file(all_item_text, ext_path)

        # Load the extracted content and split it into chunks
        if os.path.exists(ext_path):
            # print("File path:", ext_path)
            loader = TextLoader(ext_path, encoding='utf-8')
            pages = loader.load_and_split()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            docs = text_splitter.split_documents(pages)
            all_docs.extend(docs)
    embeddings = OpenAIEmbeddings()
    #embeddings = OllamaEmbeddings(model="mxbai-embed-large", show_progress=True)
    # Create a vector store from the documents
    db = Chroma.from_documents(all_docs, embeddings, persist_directory=f"{PERSIST_DIRECTORY}/{symbol}/item_7")
    logging.info(f"Vector database created for {symbol}")
    db.persist()
    return ""


def main(symbol):
    create_DB(symbol)


if __name__ == "__main__":
    symbol = input("Enter the symbol: ")
    main(symbol)
