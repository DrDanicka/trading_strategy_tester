from enum import Enum

class LLMModel(Enum):
    LLAMA_3B = 'llama3_2-3B_tst_ft'
    LLAMA_1B = 'llama3_2-1B_tst_ft'
    QWEN_0_5B = 'qwen2_5-0_5B_tst_ft'
    STRATEGY_OBJECT = 'strategy_object'
    CHAT_GPT_API = 'chat-gpt-api'

llm_model_dict = {
    'llama3_2-3B_tst_ft': LLMModel.LLAMA_3B,
    'llama3_2-1B_tst_ft': LLMModel.LLAMA_1B,
    'qwen2_5-0_5B_tst_ft': LLMModel.QWEN_0_5B,
    'strategy_object': LLMModel.STRATEGY_OBJECT,
    'chat-gpt-api': LLMModel.CHAT_GPT_API
}
