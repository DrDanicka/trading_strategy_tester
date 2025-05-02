# Large Language Model Integration

The project integrates with Large Language Models (LLMs) to help generate and optimize trading strategies from natural language descriptions.

Two main techniques are used:

## Fine-tuning

Fine-tuning involves taking a pre-trained model and training it further on a custom dataset. This allows the model to specialize in interpreting and generating trading strategy code.

The dataset consists of natural language strategy descriptions paired with their code implementations. It is created using the [`training_data`](training_data.md) module.

To learn more about fine-tuning, check the [Fine-tuning section](fine_tuning.md).

## Retrieval-Augmented Generation (RAG)

RAG enhances language model outputs by retrieving relevant information from a knowledge base during generation. In this project, RAG is used to inject context (e.g., existing strategy documentation or indicator definitions) into the LLM’s response.

The knowledge base is generated from the project’s internal documentation and strategy schema.

To learn more about RAG, check the [RAG section](rag.md).

---

## LLama

In this project we use the [LLama](https://www.llama.com) model for LLM integration. We chose this model because of its open-source nature and its ability to be fine-tuned on custom datasets.

### Running locally

To run the LLM locally we used the [Ollama](https://ollama.com) framework. Because of the hardware limitations, we used 1B and 3B Llama models which can be fine-tuned on a single GPU or Neural Engine in Apple Silicon which was our case. 

## Generating strategies

For generating strategies we use two approaches:

- First is to generate whole strategy object from natural language description. For this approach we use:
      - **Fine-tuning**: The **3B** model
      - **RAG**: The **3B** model

    This model is more capable of generating complex code which is needed for generating whole strategy object. The model is trained on a dataset of natural language descriptions and their corresponding strategy objects. 

- Second is to generate only parameters of the strategy listed in the [Strategy module](../dev/modules/strategy.md) and then combine them into the strategy object. For this approach we use:
    - **Fine-tuning**:
        - **1B** model for all of the parameters except the `buy_condition` and `sell_condition`.
        - **3B** model for the `buy_condition` and `sell_condition` parameters. This is because these parameters are more complex and require a more capable model to generate them correctly.
    - **RAG**:
        - In this case we use the **3B** model for all of the parameters. This is because RAG needs more context to generate the parameters correctly and the **3B** model is more capable of generating complex code.