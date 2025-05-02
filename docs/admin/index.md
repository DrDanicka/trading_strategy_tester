# Administrator Documentation

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

The web application is a separate project that uses the `Trading Strategy Tester` package as a backend. If you want to use the web application, you need to do the following:

1. Install `Ollama` on your machine using this [link](https://ollama.com/download).
2. Clone the repository:
```bash
git clone https://github.com/DrDanicka/trading_strategy_tester_web_app.git
```
3. Navigate to the project directory:
```bash
cd trading_strategy_tester_web_app
```
4. Initialize the `Ollama` models:
```bash
python init_ollama.py
```
This step downloads the [fine-tuned weights](https://huggingface.co/drdanicka/trading-strategy-tester-weights) for the `Llama 3.2` models that are needed to create `Ollama` models. It's required to have at least `50GB` of free space on your disk. Right after the weights are downloaded, `Ollama` models are created and the weights are deleted. 
5. Start the application with docker:
```bash
docker-compose up --build
```
This command builds the docker image and starts the application. The application will be available at [`http://localhost:5001`](http://localhost:5001).

Note: If you want to use LLM integration in your code without the web application, you still have to do steps 1-4. to initialize the models. You can then use the `process_prompt` function to generate trading strategies from natural language prompts.