from trading_strategy_tester.llm_communication.few_shot_prompting.extract_parameter import extract_parameter

def get_fsp_response(model, prompt):
    model_for = model.split('-')[-2]

    return extract_parameter(prompt, model_for)