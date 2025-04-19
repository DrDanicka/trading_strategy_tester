import json
from trading_strategy_tester.training_data.prompt_builder import PromptBuilder

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
    pb = PromptBuilder(random_seed=random_seed)

    # Open main training file and field-specific output files
    full_file = open(f"_data/full/{output_prefix}.jsonl", "w")
    field_files = {field: open(f"_data/fields/{output_prefix}_{field}.jsonl", "w") for field in FIELDS}

    for _ in range(number_of_training_data):
        pb.regenerate_bools()

        # Generate the prompt and both object formats
        prompt_text, strategy_object, strategy_object_dict = pb.generate_prompt()

        # Write the full prompt + Strategy object
        json.dump({"prompt": prompt_text, "completion": strategy_object}, full_file)
        full_file.write("\n")

        # Write each field-specific entry
        for field in FIELDS:
            field_value = strategy_object_dict.get(field, "")
            json.dump({"prompt": prompt_text, "completion": field_value}, field_files[field])
            field_files[field].write("\n")

    # Close all files
    full_file.close()
    for f in field_files.values():
        f.close()

    print(f"Saved {number_of_training_data} prompts to '{output_prefix}.jsonl'")
    print(f"Also saved per-field JSONL files with prefix '{output_prefix}_<field>.jsonl'")


# Generate sets
generate_trading_data(number_of_training_data=50_000, output_prefix="train", random_seed=42)
generate_trading_data(number_of_training_data=10_000, output_prefix="valid", random_seed=43)
generate_trading_data(number_of_training_data=10_000, output_prefix="test", random_seed=44)
