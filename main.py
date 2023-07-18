import streamlit as st
import openai

# Set up your OpenAI API credentials
openai.api_key = "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"

# Define your Streamlit app layout
def app_layout():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("Enter your symptoms or describe the problem")
    if st.button("Get Diagnosis"):
        diagnosis = get_diagnosis(user_input)
        st.write(f"Probable Diagnosis: {diagnosis}")

# Function to generate diagnosis using GPT API
def get_diagnosis(symptoms):
    # Set the GPT model and parameters
    model = "gpt-3.5-turbo"
    max_tokens = 50
    
    # Generate diagnosis using GPT API
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a healthcare assistant."},
            {"role": "user", "content": symptoms}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Extract the generated diagnosis from the API response
    diagnosis = response.choices[0].message.content.strip()
    
    return diagnosis

# Run the Streamlit app
def main():
    app_layout()

if __name__ == "__main__":
    main()
