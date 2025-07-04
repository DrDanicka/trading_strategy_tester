# Documentation for Administrators

This documentation is intended for people who want to know how to run the application locally.

## Trading Strategy Tester package

In terms of the `Trading Strategy Tester` [Python package](https://pypi.org/project/trading-strategy-tester/) itself, user can simply install it via `pip`:
```bash
pip install trading-strategy-tester
```
This will install the latest stable version of the package. If you want to install the latest development version, you can clone the repository and install it locally:
```bash
git clone https://github.com/DrDanicka/trading_strategy_tester.git
```
or if you are using Apple device with `mlx` support, you can clone this version:
```bash
git clone --recurse-submodules https://github.com/DrDanicka/trading_strategy_tester.git
```
in which you would be able to train your models locally. 

## Web Application

The web application is a separate project that uses the Trading Strategy Tester package as a backend. If you want to use the web application, you need to do the following:

- Install and start `Ollama` on your machine using this [link](https://ollama.com/download).

- Clone the repository:

```bash
git clone https://github.com/DrDanicka/trading_strategy_tester_web_app.git
```

- Navigate to the project directory:

```bash
cd trading_strategy_tester_web_app
```

- Initialize the Ollama models:

```bash
python init_ollama.py
```

This step downloads the [fine-tuned weights](https://huggingface.co/drdanicka/trading-strategy-tester-weights) for the `Llama 3.2` models that are needed to create `Ollama` models. It's required to have at least **50GB** of free space on your disk. Right after the weights are downloaded, `Ollama` models are created and the weights are deleted.

- Start the application with Docker:

```bash
docker-compose up --build
```

This command builds the Docker image and starts the application. The app will be available at [http://localhost:5001](http://localhost:5001).

Note: If you want to use LLM integration in your code without the web application, you still have to do steps 1-4. to initialize the models. You can then use the `process_prompt` function to generate trading strategies from natural language prompts.

## Training your own models

In the previous section we described how to create the `Ollama` models with already fine-tuned weights that were created for this project. It is the recommended way to use the models, but if you want to train your own models, you can do so by following these steps:

**IMPORTANT NOTE**: Training your own models is only available on Apple devices with `mlx` support. If you are using a different device, you can still use the pre-trained models from the previous section but you won't be able to train your own models.

- Install and start `Ollama` on your machine using this [link](https://ollama.com/download).

- Clone the repository:

```bash
git clone --recurse-submodules https://github.com/DrDanicka/trading_strategy_tester.git
```

- Navigate to the `trading_strategy_tester/evaluation` directory:

```bash
cd trading_strategy_tester/evaluation
```

- Create your own training data with training data generator:

```bash
python3 ../trading_strategy_tester/training_data/training_data.py
```

You can also change the counts and seeds of the training data generator in the `trading_strategy_tester/training_data/training_data.py` file.

- Train the models with the generated training data:

```bash
python train.py --model all
```

This command trains all the models with the generated training data. You can also train only specific models by using the `--model` option and you can also change learning rage, iterations, and other parameters. You can find them in the `train.py` file.

After the training is finished, you have all the models created in `Ollama` and you can use them in your code or in the web application.