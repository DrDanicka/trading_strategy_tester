import argparse
from train_model import single_model_train

def train_all_models(learning_rate=1e-5, iters=100, fine_tune_type="full", skip_training=False):
    names = [
        'llama3-2-1B_tst_ft-ticker',
        'llama3-2-1B_tst_ft-position_type',
        'llama3-2-1B_tst_ft-stop_loss',
        'llama3-2-1B_tst_ft-take_profit',
        'llama3-2-1B_tst_ft-start_date',
        'llama3-2-1B_tst_ft-end_date',
        'llama3-2-1B_tst_ft-period',
        'llama3-2-1B_tst_ft-interval',
        'llama3-2-1B_tst_ft-initial_capital',
        'llama3-2-1B_tst_ft-order_size',
        'llama3-2-1B_tst_ft-trade_commissions',
        'llama3-2-3B_tst_ft-conditions',
        'llama3-2-3B_tst_ft-all',
    ]

    for name in names:
        model_for = name.split('-')[-1]

        if model_for == 'all':
            model_path = '_data/full/'
        else:
            model_path = f'_data/fields/{model_for}/'

        if '1B' in name:
            model = 'meta-llama/Llama-3.2-1B-Instruct'
        else:
            model = 'meta-llama/Llama-3.2-3B-Instruct'

        print(f"Training {name} with model {model} on data from {model_path}")
        single_model_train(
            model=model,
            data=model_path,
            learning_rate=learning_rate,
            iters=iters,
            fine_tune_type=fine_tune_type,
            name=name,
            skip_training=skip_training
        )

def main():
    parser = argparse.ArgumentParser(description="One-click LoRA training, fusing, and GGUF/ollama export")
    parser.add_argument('--model', required=True, help='Path or name of the base model')
    parser.add_argument('--data', help='Path to training data')
    parser.add_argument('--learning-rate', type=float, default=1e-5, help='Learning rate for training')
    parser.add_argument('--iters', type=int, default=100, help='Number of training iterations')
    parser.add_argument('--fine-tune-type', default="full", help='Fine-tune type (default: full)')
    parser.add_argument('--name', help='Name of the final model (used for GGUF and ollama)')
    parser.add_argument('--skip-training', action='store_true', help='Skip training step')

    args = parser.parse_args()

    if args.model == "all":
        train_all_models(
            learning_rate=args.learning_rate,
            iters=args.iters,
            fine_tune_type=args.fine_tune_type,
            skip_training=args.skip_training
        )
    else:
        if not args.data or not args.name:
            raise ValueError("You must provide --data and --name when training a single model!")
        single_model_train(
            args.model,
            args.data,
            args.learning_rate,
            args.iters,
            args.fine_tune_type,
            args.name,
            skip_training=args.skip_training
        )

if __name__ == "__main__":
    main()