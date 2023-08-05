import openai
import pdfplumber

# Set up OpenAI API credentials
openai.api_key = "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"

# Define function to perform zero-shot learning with GPT-3
def zero_shot_gpt3(prompt, model):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        presence_penalty=0,
        frequency_penalty=0
    )
    return response.choices[0].text.strip()

# Define function to prompt user for question and return response
def docai(model, prompt):
    while True:
        user_input = input("What's your question? (Type 'exit' to quit)\n")
        if user_input.lower() == 'exit':
            break
        question_prompt = f"Answer the following question about the Caduceus app:\n\n{user_input}\n\nAnswer:"
        full_prompt = prompt + question_prompt
        answer = zero_shot_gpt3(full_prompt, model)
        print(answer)

# Read the text from the PDF file and store it as a string variable
with pdfplumber.open('/home/user/.config/spyder-py3/caduceus.pdf') as pdf:
    text = ''
    for page in pdf.pages:
        text += page.extract_text()

# Run with the text from the PDF file as the prompt
model = 'text-davinci-003'
docai(model, text)

