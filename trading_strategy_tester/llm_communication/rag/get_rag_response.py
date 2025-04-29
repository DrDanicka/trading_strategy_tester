from trading_strategy_tester.llm_communication.rag.extract_parameter import extract_parameter

def get_rag_response(model, prompt):
    model_for = model.split('-')[-2]

    return extract_parameter(prompt, model_for)