import ollama

def extract_parameter(description, parameter):
    with open(f"rag/prompts/{parameter}_prompt.txt", "r") as file:
        parameter_prompt = file.read()

    prompt = parameter_prompt.format(description=description)
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        options={
            "temperature": 0,
        }
    )

    return response
