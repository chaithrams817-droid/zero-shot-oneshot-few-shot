
from prompt_analyzer import analyze_prompt

test_prompts = [
    "Explain DBMS.",
    "Example: Input: 2, Output: 4. Explain the pattern.",
    "Act as a Python teacher. Explain loops.",
]

for prompt in test_prompts:
    result = analyze_prompt(prompt)

    print("\nPrompt:", prompt)
    print("Techniques:", result["techniques"])
    print("Explanation:", result["explanation"])
