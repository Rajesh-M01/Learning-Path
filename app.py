import streamlit as st
from transformers import pipeline, set_seed
import re

st.set_page_config(page_title="AI Learning Path Generator", page_icon="📚")
st.title("📚 AI-Powered Personalized Learning Path")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()
set_seed(42)

resources = {
    "Python": "https://realpython.com/",
    "C++": "https://cplusplus.com/doc/tutorial/",
    "Java": "https://docs.oracle.com/javase/tutorial/",
    "DBMS": "https://www.geeksforgeeks.org/dbms/",
    "SQL": "https://sqlzoo.net/",
    "OOP": "https://www.geeksforgeeks.org/object-oriented-programming-in-cpp/"
}

subject = st.selectbox("Choose a subject/topic", list(resources.keys()))
goal = st.selectbox("Your learning goal", [
    "Crack coding interviews", "Build real-world projects", "Understand core concepts", "Learn from scratch"
])
daily_time = st.selectbox("How much time can you study per day?", ["30 mins", "1 hour", "2 hours", "3+ hours"])

if st.button("Generate Learning Path"):
    with st.spinner("Generating your personalized plan..."):
        prompt = (
            f"Create a 4-week study plan for {subject} to help a student who wants to {goal} "
            f"and can study {daily_time} daily. Provide clear weekly tasks, and include this official learning resource: {resources[subject]}. "
            "Avoid fake or made-up links. Format clearly with weeks and bullet points."
        )

        try:
            result = generator(prompt, max_new_tokens=250)[0]["generated_text"]
            output = result.replace(prompt, "").strip()
            output = re.sub(r'http\S+', '', output)
            output += f"\n\n🔗 Recommended Resource: {resources[subject]}"

            st.success("✅ Here's your personalized learning path!")
            st.markdown("---")
            st.markdown(output)

        except Exception as e:
            st.error(f"❌ Error: {e}")
