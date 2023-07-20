import streamlit as st
import openai

# Set up your OpenAI API credentials
openai.api_key = "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"

# Define your Streamlit app layout
def app_layout():
    st.title("DiagnoSAGE")
    st.title("Healthcare Assistant")
    user_input = st.text_input("Enter your symptoms or describe the problem")
    if st.button("Get Diagnosis"):
        response = get_diagnosis_response(user_input)
        st.write(f"{response}")

        # Ask for user feedback
        feedback = st.text_area("Provide feedback on the response:", "")

        # If feedback is given, use it for updating the model
        if feedback:
            update_model(response, feedback)

# Function to generate diagnosis and precautions using GPT API with few-shot learning
def get_diagnosis_response(symptoms):
    # Set the GPT model and parameters
    model = "gpt-3.5-turbo"
    max_tokens = 200

    # Define a few-shot learning prompt with an example
    prompt = """
    Examples:
    Symptom: I have a fever and cough.
    Diagnosis: flu
    Precautions: Rest, drink plenty of fluids, and take fever-reducing medications.

    Symptom: My joints are painful and swollen.
    Diagnosis: arthritis
    Precautions: Avoid strenuous activities and use joint support.

    Symptom: I have a sore throat and runny nose.
    Diagnosis: common_cold
    Precautions: Rest, drink warm fluids, and take over-the-counter cold medicine.
    
    Symptom: {}""".format(symptoms)

    # Generate response using GPT API
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a healthcare assistant. You will be given a description of symptoms the patient is suffering from, give a possible diagnosis, precautions and a caution to seek real medical advice. Do this in less than 200 words. Give the response in this format Possible Diagnosis:\n Precautions:\n Caution:"},
            {"role": "user", "content": symptoms}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated response from the API
    generated_text = response.choices[0].message["content"].strip()

    return generated_text

# Function to update the model with user feedback
def update_model(input_text, feedback):
    # Set the GPT model and parameters
    model = "gpt-3.5-turbo"
    max_tokens = 5  # Set the number of tokens for the feedback prompt

    # Generate response using GPT API with the feedback loop
    openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a healthcare assistant. You will be given a description of symptoms the patient is suffering from, give a possible diagnosis, precautions and a caution to seek real medical advice. Do this in less than 200 words. Give the response in this format Possible Diagnosis:\n Precautions:\n Caution:"},
            {"role": "user", "content": input_text},
            {"role": "system", "content": feedback}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0  # Set temperature to 0 to make the feedback explicit
    )

# Run the Streamlit app
def main():
    app_layout()

if __name__ == "__main__":
    main()
