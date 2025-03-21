from enum import Enum

class LLMModel(Enum):
    LLAMA_1B = 'llama3_2-1B_tst_ft'
    QWEN_0_5B = 'qwen2_5-0_5B_tst_ft'
    CHAT_GPT_API = 'chat-gpt-api'

llm_model_dict = {
    'llama3_2-1B_tst_ft': LLMModel.LLAMA_1B,
    'qwen2_5-0_5B_tst_ft': LLMModel.QWEN_0_5B,
    'chat-gpt-api': LLMModel.CHAT_GPT_API
}
