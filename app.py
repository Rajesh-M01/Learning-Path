import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Learning Path Recommender", page_icon="📚")
st.title("📚 AI-Powered Personalized Learning Path Generator")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="tiiuae/falcon-7b-instruct", tokenizer="tiiuae/falcon-7b-instruct")

generator = load_model()

# Inputs
st.markdown("Fill in your learning preferences to get a custom study plan.")
subject = st.selectbox("Choose a subject/topic", ["Python", "Java", "C++", "Data Structures", "DBMS", "SQL", "OOP"])
goal = st.selectbox("Your learning goal", [
    "Crack coding interviews", "Build real-world projects", "Understand concepts", "Learn from scratch"
])
daily_time = st.selectbox("How much time can you study per day?", ["30 mins", "1 hour", "2 hours", "3+ hours"])

if st.button("Generate My Learning Path"):
    with st.spinner("Generating your personalized plan..."):
        prompt = (
            f"Create a personalized {subject} study plan to help a student who wants to '{goal}' "
            f"and can study '{daily_time}' daily. Split the content into a clear weekly learning roadmap. "
            f"Include what to learn each week and mention resources like videos, articles or exercises."
        )

        try:
            result = generator(prompt, max_new_tokens=512)[0]["generated_text"]
            output = result.replace(prompt, "").strip()

            st.success("✅ Here's your personalized learning path!")
            st.markdown("---")
            st.markdown(output)

        except Exception as e:
            st.error(f"❌ Failed to generate learning plan. Error: {e}")
