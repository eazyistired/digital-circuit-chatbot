import sys
import gradio as gr
import json

sys.path.append("digital-circuit-chatbot-gui")
sys.path.append("digital-circuit-chatbot-api")

from demo_ui import create_demo_ui
from main_api import get_qa_chain, generate_response

demo, chat_history, text_input, uploaded_files, retrieved_docs, submit_btn = (
    create_demo_ui()
)
qa_chain = get_qa_chain()


def add_text(chat_history, text):
    chat_history.append((text, ""))

    return chat_history


def get_response(query, chat_history):
    chain_result = qa_chain.invoke(
        {"query": query},
        return_only_outputs=True,
    )

    print(f"Chain results: \n {chain_result} \n\n")

    answer = chain_result["result"].split("[/INST]")[-1]
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
    # submit_btn.click(get_response, inputs=[text_input], outputs=[chatbot])


if __name__ == "__main__":
    demo.queue()
    demo.launch(debug=True)
