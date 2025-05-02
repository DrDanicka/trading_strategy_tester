# Fine-tuning

**Fine-tuning** is a powerful techinigue that allows us to adapt a pre-trained language model to a specific task or domain. In the context of this project, we use fine-tuning to improve the performance of the LLM in generating trading strategies based on natural language descriptions.

## What model do we use?

We use the [Llama 3.2](https://www.llama.com) model for fine-tuning. The models we use come in two sizes:

- **Llama 3.2 1B**: A smaller model that is faster and requires less memory, but may not perform as well on complex tasks.
- **Llama 3.2 3B**: A larger model that is slower and requires more memory, but performs better on complex tasks.

## How do we fine-tune the model?

In this project we used `mlx-lm` framework for fine-tuning the model. The `mlx-lm` framework is a powerful tool for training and deploying large language models. It provides a simple and flexible API for fine-tuning models on custom datasets. It is only available for Apple devices with `mlx` support.

If you have an Apple device with `mlx` support you can train your models locally as well. Here are the steps to do it:
1. Clone the repository:
   ```bash
   git clone --recurse-submodules https://github.com/DrDanicka/trading_strategy_tester.git
    ```
2. Navigate to the evaluation directory:
   ```bash
   cd trading_strategy_tester/evaluation
   ```
   and install the required dependencies:
   ```bash
    pip install -r requirements.txt
    ```
3. Run `train.py` script:
   ```bash
   python train.py --model all 
   ```
   This will train all the models needed for the project. 

If you don't want to train the models you can still download them as written in [Administrator Documentation](../admin/index.md). You still have to have `Ollama` installed on your machine because the models are exported to `Ollama`. How to do it is also written in the [Administrator Documentation](../admin/index.md).

## What is the dataset?

The dataset used for fine-tuning the model consists of natural language descriptions of trading strategies paired with their corresponding code implementations. The dataset is created using the [`training_data`](training_data.md) module.