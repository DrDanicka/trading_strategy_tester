import argparse
import ollama
import pandas as pd
import os
import json
from trading_strategy_tester.llm_communication.rag.get_rag_response import get_rag_response

# --- Model List ---
ollama_models = [
    # 'llama3-2-1B_tst_ft-ticker',
    # 'llama3-2-1B_tst_ft-position_type',
    # 'llama3-2-1B_tst_ft-stop_loss',
    # 'llama3-2-1B_tst_ft-take_profit',
    # 'llama3-2-1B_tst_ft-start_date',
    # 'llama3-2-1B_tst_ft-end_date',
    # 'llama3-2-1B_tst_ft-period',
    # 'llama3-2-1B_tst_ft-interval',
    # 'llama3-2-1B_tst_ft-initial_capital',
    # 'llama3-2-1B_tst_ft-order_size',
    # 'llama3-2-1B_tst_ft-trade_commissions',
    'llama3-2-3B_tst_ft-conditions',
    # 'llama3-2-3B_tst_ft-all',
    # 'llama3-2-ticker-rag',
    # 'llama3-2-position_type-rag',
    # 'llama3-2-stop_loss-rag',
    # 'llama3-2-take_profit-rag',
    # 'llama3-2-start_date-rag',
    # 'llama3-2-end_date-rag',
    # 'llama3-2-period-rag',
    # 'llama3-2-interval-rag',
    # 'llama3-2-initial_capital-rag',
    # 'llama3-2-order_size-rag',
    # 'llama3-2-trade_commissions-rag',
    # 'llama3-2-conditions-rag',
    # 'llama3-2-all-rag',
]


# --- Core processing function ---
def process_model(model, data_path):
    os.makedirs('testing_outputs', exist_ok=True)

    client = ollama.Client()
    model_for = model.split('-')[-1]
    is_rag = False

    if model_for == 'rag':
        is_rag = True
        model_for = model.split('-')[-2]

    if data_path:
        data = pd.read_json(path_or_buf=data_path, lines=True)
    else:
        if model_for == 'all':
            data = pd.read_json(path_or_buf='_data/full/test.jsonl', lines=True)
        else:
            data = pd.read_json(path_or_buf=f'_data/fields/{model_for}/test.jsonl', lines=True)

    output_file = f'testing_outputs/{model}.jsonl'
    number_of_test_cases = len(data)

    if os.path.exists(output_file):
        existing_record = pd.read_json(output_file, lines=True)
        if len(existing_record) >= len(data):
            print(f"Skipping {model}, already processed all entries.")
            return
        if len(existing_record) > 0:
            print(
                f"Model {model} already partially processed {len(existing_record)} entries. Continuing from {len(existing_record)}.")
            data = data.iloc[len(existing_record):]

    print(f'Running model {model} on {len(data)} entries.')

    with open(output_file, 'a') as f:
        for index, row in data.iterrows():
            if index % 100 == 0:
                print(f'Model {model}: Processing {index}/{number_of_test_cases}')

            prompt = row['prompt']
            completion = row['completion']

            if is_rag:
                response = get_rag_response(model, prompt)
            else:
                response = client.generate(
                    model=model,
                    prompt=prompt,
                    options={'temperature': 0},
                )

            response = response.response.strip()

            # Handle rag returning None
            if str.lower(response).endswith('none'):
                response = ''

            output_record = {
                'prompt': prompt,
                'completion': completion,
                'response': response
            }
            f.write(json.dumps(output_record) + '\n')

    print(f"Finished processing {model}. Output saved to {output_file}")


# --- Entry point ---
def main():
    parser = argparse.ArgumentParser(description="Test fine-tuned or RAG Ollama models against test data")
    parser.add_argument('--model', required=True, help="Model name to test or 'all' for batch testing")
    parser.add_argument('--data', help="(Required if model != all) Path to test data file")

    args = parser.parse_args()

    if args.model == 'all':
        for model in ollama_models:
            process_model(model, None)
    else:
        if args.model not in ollama_models:
            raise ValueError(f"Model '{args.model}' not found in ollama_models list!")

        if not args.data:
            raise ValueError("--data argument is required when testing a single model.")

        process_model(args.model, args.data)


if __name__ == "__main__":
    main()
