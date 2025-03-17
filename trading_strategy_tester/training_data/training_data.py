import json
from trading_strategy_tester.training_data.prompt_builder import PromptBuilder

def generate_trading_data(number_of_training_data: int, output_file="trading_data.jsonl"):

    pb = PromptBuilder()
    with open(output_file, "w") as f:
        for _ in range(number_of_training_data):
            pb.regenerate_bools()

            # Generate the prompt
            prompt_text, strategy_object = pb.generate_prompt()

            # Format as JSONL (one JSON object per line)
            json.dump({"prompt": prompt_text, "completion": strategy_object}, f)
            f.write("\n")  # Newline for JSONL format

    print(f'Saved {number_of_training_data} training data to {output_file}.')

# generate_trading_data(number_of_training_data=100_000, output_file="training_data.jsonl")
generate_trading_data(number_of_training_data=100_000, output_file="train.jsonl")