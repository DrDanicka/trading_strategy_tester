import json
import os

from trading_strategy_tester.training_data.prompt_builder import PromptBuilder

# List of strategy object fields that will be saved individually
FIELDS = [
    "ticker",
    "position_type",
    "conditions",
    "stop_loss",
    "take_profit",
    "start_date",
    "end_date",
    "period",
    "interval",
    "initial_capital",
    "order_size",
    "trade_commissions",
]

def generate_trading_data(number_of_training_data: int, output_prefix: str = "train", random_seed: int = 42):
    """
    Generate synthetic trading strategy prompts and save them to JSONL files.

    It produces:
      - A full prompt-to-strategy mapping.
      - Separate per-field JSONL files for each strategy component.

    :param number_of_training_data: Number of training samples to generate.
    :param output_prefix: Prefix used for output file names (e.g., 'train', 'valid', 'test').
    :param random_seed: Random seed for reproducibility.
    """
    # Initialize PromptBuilder with a fixed random seed
    pb = PromptBuilder(random_seed=random_seed)

    script_dir = os.path.dirname(__file__)
    data_path = os.path.join(script_dir, '..', '..', 'evaluation', '_data')
    fields_dir = os.path.join(data_path, 'fields')
    full_dir = os.path.join(data_path, 'full')

    os.makedirs(full_dir, exist_ok=True)
    os.makedirs(fields_dir, exist_ok=True)

    # Open main JSONL file for full training data
    full_file = open(os.path.join(full_dir, f'{output_prefix}.jsonl'), "w")

    # Open separate JSONL files for each field
    field_files = {}
    for field in FIELDS:
        #field_dir = f"_data/fields/{field}"
        field_dir = os.path.join(fields_dir, field)
        os.makedirs(field_dir, exist_ok=True)
        field_files[field] = open(os.path.join(field_dir, f"{output_prefix}.jsonl"), "w")
        #field_files[field] = open(f"{field_dir}/{output_prefix}.jsonl", "w")

    # Generate training samples
    for _ in range(number_of_training_data):
        pb.regenerate_bools()

        # Generate prompt text, Strategy object text, and field values dictionary
        prompt_text, strategy_object, strategy_object_dict = pb.generate_prompt()

        # Save the full prompt and complete Strategy object
        json.dump({"prompt": prompt_text, "completion": strategy_object}, full_file)
        full_file.write("\n")

        # Save each field separately
        for field in FIELDS:
            field_value = strategy_object_dict.get(field, "")
            json.dump({"prompt": prompt_text, "completion": field_value}, field_files[field])
            field_files[field].write("\n")

    # Close all output files
    full_file.close()
    for f in field_files.values():
        f.close()

    print(f"Saved {number_of_training_data} prompts to evaluation module '_data/full/{output_prefix}.jsonl'")
    print(f"Also saved per-field JSONL files under evaluation module '_data/fields/<field>/{output_prefix}.jsonl'")

if __name__ == "__main__":
    # Generate training, validation, and testing datasets
    generate_trading_data(number_of_training_data=50_000, output_prefix="train", random_seed=42)
    generate_trading_data(number_of_training_data=10_000, output_prefix="valid", random_seed=43)
    generate_trading_data(number_of_training_data=10_000, output_prefix="test", random_seed=44)
