import openai

class LLMProvider:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        """Initialize the LLM provider with an API key and model."""
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def generate_text(self, prompt, max_tokens=100, temperature=0.7):
        """Generate text from the LLM based on a prompt."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating text: {e}")
            return None