# Large Language Model Integration

The project integrates with Large Language Models (LLMs) to help generate and optimize trading strategies from natural language descriptions.

Two main techniques are used:

## Fine-tuning

Fine-tuning involves taking a pre-trained model and training it further on a custom dataset. This allows the model to specialize in interpreting and generating trading strategy code.

The dataset consists of natural language strategy descriptions paired with their code implementations. It is created using the [`training_data`](training_data.md) module.

## Retrieval-Augmented Generation (RAG)

RAG enhances language model outputs by retrieving relevant information from a knowledge base during generation. In this project, RAG is used to inject context (e.g., existing strategy documentation or indicator definitions) into the LLM’s response.

The knowledge base is generated from the project’s internal documentation and strategy schema.

---

## LLama

In this project we use the [LLama](https://www.llama.com) model for LLM integration. We chose this model because of its open-source nature and its ability to be fine-tuned on custom datasets.

### Running locally

To run the LLM locally we used the [Ollama](https://ollama.com) framework. Because of the hardware limitations, we used 1B and 3B Llama models which can be fine-tuned on a single GPU or Neural Engine in Apple Silicon which was our case. 