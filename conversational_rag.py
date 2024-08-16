from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# https://python.langchain.com/v0.1/docs/use_cases/question_answering/chat_history/#chain-with-chat-history

store = {}
temp_session_id = "abc123"
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

class ChatLog():
    def logger():
        return store[temp_session_id]
    
    
class ConversationalRAGChain():
    def __init__(self, rag_chain, input) -> None:
        self.rag_chain = rag_chain
        # self.get_session_history = get_session_history
        self.input = input
    
    def chain(self):
        conversational_rag_chain = RunnableWithMessageHistory(
            self.rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )
        response = conversational_rag_chain.invoke(
            {"input": self.input},
            config={
                "configurable": {"session_id": temp_session_id}
            },  # constructs a key "abc123" in `store`.
        )

        return response

