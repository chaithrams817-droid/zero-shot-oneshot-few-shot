
from prompt_improver import improve_prompt, generate_response

original_prompt = "Explain deadlock"

print("ORIGINAL PROMPT:")
print(original_prompt)

print("\nIMPROVED PROMPT:")
improved = improve_prompt(original_prompt)
print(improved)

if improved.startswith("Unable to generate a response."):
    print("\nPlease fix the Ollama connection before continuing.")
else:
    print("\nGENERATED OUTPUT FOR IMPROVED PROMPT:")
    print(generate_response(improved))
