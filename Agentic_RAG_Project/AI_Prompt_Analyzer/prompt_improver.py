
import ollama


MODEL = "qwen3:1.7b"


def generate_response(prompt):
    """Generate a response to the given prompt using Ollama."""

    try:
        result = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return result["message"]["content"].strip()

    except Exception as error:
        return (
            "Unable to generate a response. "
            f"Please check that Ollama is running and "
            f"the model '{MODEL}' is installed. Details: {error}"
        )


def improve_prompt(original_prompt):
    """Ask the local LLM to rewrite the user's prompt."""

    improvement_instruction = f"""
You are an expert prompt engineer.

Improve the user's prompt so that it is clearer, more specific,
and more useful.

Instructions:
- Infer the likely subject and purpose from the original prompt.
- Do not ask the user to assign a role manually.
- Add a suitable role only when it helps the task.
- Specify the expected answer format when useful.
- Preserve the user's original intention.
- Do not invent requirements unrelated to the request.
- Return only the improved prompt, without explanations.

Original prompt:
{original_prompt}
"""

    return generate_response(improvement_instruction)
