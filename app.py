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
            f"Generate a 4-week beginner-friendly study plan to learn {subject}. "
            f"The goal is: {goal}. The student can study {daily_time} every day. "
            "Format it clearly like:\n"
            "Week 1:\n- Topic 1\n- Topic 2\nWeek 2:\n- Topic 3\n...\n"
            f"End by recommending this link: {resources[subject]}"
        )

        try:
            result = generator(prompt, max_new_tokens=300)[0]["generated_text"]
            output = result.replace(prompt, "").strip()

            # Extract only "Week" blocks
            weeks = re.findall(r"(Week\s\d+:(?:.*?)(?=Week\s\d+:|$))", output, re.DOTALL)
            cleaned = "\n\n".join(weeks).strip()
            if not cleaned:
                cleaned = output

            cleaned += f"\n\n🔗 Recommended Resource: {resources[subject]}"

            st.success("✅ Here's your personalized learning path!")
            st.markdown("---")
            st.markdown(cleaned)

        except Exception as e:
            st.error(f"❌ Error: {e}")
