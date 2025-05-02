# Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is a technique that combines the strengths of large language models (LLMs) with external knowledge sources to improve the quality and relevance of generated content. In this project, RAG is used to enhance the generation of trading strategies by providing context and information from a knowledge base during the generation process.

## How does RAG work?

In RAG, the generation is done by base model `LLama 3.2`. We use the same prompts as in the fine-tuning process, but we also provide additional context from a knowledge base. The knowledge base is created from the project’s internal documentation and strategy schema. This allows the model to retrieve relevant information and use it to generate more accurate and contextually relevant responses.

## Prompts

For every parameter that we want to generate using RAG, we have [templates](https://github.com/DrDanicka/trading_strategy_tester/tree/main/trading_strategy_tester/llm_communication/rag/prompts) with contex and knowledge base for given parameter. The final prompt than consists of:

1. **Context and Knowledge base**: This is the context that is provided to the model. It contains information about the parameter that we want to generate. The context is created from the project’s internal documentation and strategy schema.
2. **Natural Language Prompt**: This is the natural language description of a strategy from which we want to generate the parameter. The prompt is created using the same templates as in the fine-tuning process.

In some cases it also helps to provide som examples of prompts and responses. 