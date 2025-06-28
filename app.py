import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="AI Learning Path Recommender", page_icon="📚")
st.title("📚 AI-Powered Personalized Learning Path Generator")

# Load lightweight GPT2
@st.cache_resource
def load_model():
    model = pipeline("text-generation", model="gpt2")
    return model

generator = load_model()
set_seed(42)

# UI
st.markdown("Fill in your learning preferences to get a custom study plan.")
subject = st.selectbox("Choose a subject/topic", ["Python", "Java", "C++", "Data Structures", "DBMS", "SQL", "OOP"])
goal = st.selectbox("Your learning goal", [
    "Crack coding interviews", "Build real-world projects", "Understand concepts", "Learn from scratch"
])
daily_time = st.selectbox("How much time can you study per day?", ["30 mins", "1 hour", "2 hours", "3+ hours"])

if st.button("Generate My Learning Path"):
    with st.spinner("Generating your personalized plan..."):
        prompt = (
            f"Create a personalized weekly study plan for {subject} to help a student who wants to {goal} "
            f"and can study {daily_time} daily. Suggest weekly tasks and free resources if possible."
        )

        try:
            result = generator(prompt, max_new_tokens=250)[0]["generated_text"]
            output = result.replace(prompt, "").strip()

            st.success("✅ Here's your personalized learning path!")
            st.markdown("---")
            st.markdown(output)

        except Exception as e:
            st.error(f"❌ Error: {e}")
