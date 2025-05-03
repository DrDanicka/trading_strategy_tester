import ollama
import os

def extract_parameter(description, parameter):
    script_dir = os.path.dirname(__file__)
    prompt_path = os.path.join(script_dir, 'prompts', f"{parameter}_prompt.txt")

    with open(prompt_path, "r") as file:
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
