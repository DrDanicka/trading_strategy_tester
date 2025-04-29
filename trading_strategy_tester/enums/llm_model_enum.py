from enum import Enum

class LLMModel(Enum):
    LLAMA_ALL = 'llama3-2-3B_tst_ft-all'
    LLAMA_FIELDS = 'llama3-2-1B_tst_ft-'
    LLAMA_ALL_RAG = 'llama3-2-all-rag'
    LLAMA_FIELDS_RAG = 'llama3-2-fields-rag'
    STRATEGY_OBJECT = 'strategy_object'

llm_model_dict = {
    'llama3-2-3B_tst_ft-all': LLMModel.LLAMA_ALL,
    'llama3-2-1B_tst_ft-': LLMModel.LLAMA_FIELDS,
    'strategy_object': LLMModel.STRATEGY_OBJECT,
    'llama3-2-all-rag': LLMModel.LLAMA_ALL_RAG,
    'llama3-2-fields-rag': LLMModel.LLAMA_FIELDS_RAG,
}
