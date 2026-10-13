
import re


def analyze_prompt(prompt):
    """Identify common prompting techniques in a user's prompt."""

    text = prompt.strip()

    if not text:
        return {
            "techniques": [],
            "explanation": "Please enter a prompt to analyze."
        }

    # Detect explicit role instructions.
    role_patterns = [
        r"\byou are\b",
        r"\bact as\b",
        r"\bassume the role of\b",
        r"\bpretend to be\b"
    ]

    has_role = any(
        re.search(pattern, text, re.IGNORECASE)
        for pattern in role_patterns
    )

    # Detect common example indicators.
    example_patterns = [
        r"\bfor example\s*:",
        r"\bexample\s*:",
        r"\binput\s*:",
        r"\boutput\s*:",
        r"\binput\s*->",
        r"\binput\s*=>"
    ]

    example_count = sum(
        len(re.findall(pattern, text, re.IGNORECASE))
        for pattern in example_patterns
    )

    # Avoid counting the same example twice.
    example_count = min(example_count, 3)

    if example_count >= 2:
        techniques = ["Few-shot prompting"]
        explanation = (
            "Multiple example indicators were detected. "
            "The prompt may demonstrate the desired response pattern."
        )
    elif example_count == 1:
        techniques = ["One-shot prompting"]
        explanation = (
            "One example indicator was detected. "
            "The prompt may demonstrate the desired response pattern."
        )
    else:
        techniques = ["Zero-shot prompting"]
        explanation = (
            "No clear example indicators were detected. "
            "The prompt appears to rely on instructions alone."
        )

    if has_role:
        techniques.append("Role prompting")
        explanation += " The prompt also assigns a role to the model."

    return {
        "techniques": techniques,
        "explanation": explanation
    }
