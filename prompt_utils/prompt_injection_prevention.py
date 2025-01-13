import re

class PromptHandler:
    @staticmethod
    def prevent_injection(prompt: str) -> str:
        """
        Prevent prompt injection by sanitizing and validating the user input.
        """
        # Remove dangerous patterns (e.g., injection attacks)
        prompt = re.sub(r"(ignore|bypass|shutdown|execute|delete|remove|system)", "", prompt, flags=re.IGNORECASE)

        # Limit the length of the prompt
        max_length = 500
        if len(prompt) > max_length:
            prompt = prompt[:max_length]

        # Ensure the prompt is alphanumeric with limited symbols
        allowed_chars = re.compile(r"[^a-zA-Z0-9\s.,?!']")
        prompt = allowed_chars.sub("", prompt)

        return prompt.strip()

    @staticmethod
    def validate_prompt(prompt: str) -> bool:
        """
        Validate if the prompt contains forbidden or suspicious phrases.
        """
        forbidden_phrases = [
            "shutdown the system",
            "access admin data",
            "malicious code",
            "execute commands",
        ]
        for phrase in forbidden_phrases:
            if phrase.lower() in prompt.lower():
                return False
        return True
