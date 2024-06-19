import sys
import gradio as gr
import json
import os

sys.path.append("digital-circuit-chatbot-gui")
sys.path.append("digital-circuit-chatbot-api")

from demo_ui import create_demo_ui
from main_api import get_qa_chain, generate_response, get_vector_database_from_path

# project_dir_path = os.path.dirname(__file__)

# vector_database_path = vector_database_path = os.path.join(
#     project_dir_path, "database", "vector_store"
# )
# embedding_model_path = os.path.join(project_dir_path, "models", "instructor-xl")

demo, chat_history, text_input, retrieved_docs, submit_btn = create_demo_ui()

# embedding_model = get_embedding_model_from_path(embedding_model_path)
# vector_database = get_vector_database_from_path(vector_database_path)

qa_chain = get_qa_chain()


def add_text(chat_history, text):
    chat_history.append((text, ""))

    return chat_history


# def upload_files(files: list):
#     print(f"\n\nFiles uploaded: {files}\n\n")

#     return []


def get_response(query, chat_history):
    chain_result = qa_chain.invoke(
        {"question": query, "chat_history": [], "ceva": str(chat_history)},
        return_only_outputs=True,
    )

    print(f"Chain results: \n {chain_result} \n\n")

    answer = chain_result["answer"].split("[/INST]")[-1]
    # answer = chain_result["answer"]
    chat_history.append((query, answer))

    source_documents = list(chain_result["source_documents"])

    retrieved_docs = ""
    for source_document in source_documents:
        retrieved_docs += source_document.page_content + "\n\n"

    # response = chain_result["result"].split("[/INST]")[1]
    # chat_history.append((query, response))

    # print(chain_result["source_documents"])
    # source_documents = list(chain_result["source_documents"])

    # retrieved_docs = ""
    # for source_document in source_documents:
    #     print(source_document.page_content)
    #     print("\n\n\n")
    #     retrieved_docs += source_document.page_content + "\n\n"

    return "", chat_history, retrieved_docs


# def load_retrieved_docs(source_documents):
#     retrieved_text = ""
#     for source_document in source_documents:
#         retrieved_text += str(source_document.page_content) + "\n"

#     retrieved_docs.value = retrieved_text


with demo:
    text_input.submit(
        get_response,
        inputs=[text_input, chat_history],
        outputs=[text_input, chat_history, retrieved_docs],
    )

    # uploaded_files.upload(
    #     fn=upload_files, inputs=uploaded_files, outputs=[uploaded_files]
    # )

    submit_btn.click(
        get_response,
        inputs=[text_input, chat_history],
        outputs=[text_input, chat_history, retrieved_docs],
    )


if __name__ == "__main__":
    demo.queue()
    demo.launch(debug=True)
