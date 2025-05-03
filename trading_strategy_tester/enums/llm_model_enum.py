from enum import Enum

class LLMModel(Enum):
    LLAMA_ALL = 'llama3-2-3B_tst_ft-all'
    LLAMA_FIELDS = 'llama3-2-1B_tst_ft-'
    LLAMA_ALL_FSP = 'llama3-2-all-fsp'
    LLAMA_FIELDS_FSP = 'llama3-2-fields-fsp'
    STRATEGY_OBJECT = 'strategy_object'

llm_model_dict = {
    'llama3-2-3B_tst_ft-all': LLMModel.LLAMA_ALL,
    'llama3-2-1B_tst_ft-': LLMModel.LLAMA_FIELDS,
    'strategy_object': LLMModel.STRATEGY_OBJECT,
    'llama3-2-all-fsp': LLMModel.LLAMA_ALL_FSP,
    'llama3-2-fields-fsp': LLMModel.LLAMA_FIELDS_FSP,
}
