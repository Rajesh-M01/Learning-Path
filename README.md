# Learning-Path

# AI Learning Path Recommender

An AI-powered app that generates personalized learning plans based on the user's subject, goal, and available study time.

## Features

- Choose from multiple subjects (Python, C++, Java, DBMS, etc.)
- Set your learning goal and daily study time
- Get a weekly learning roadmap tailored to your needs
- AI-generated suggestions using GPT2

## Tech Stack

- Python
- Streamlit
- Hugging Face Transformers (GPT2)
- Deployed on Streamlit Cloud

## AI Usage

The app uses a pre-trained GPT2 model via Hugging Face’s Transformers pipeline. It generates structured study plans from custom prompts based on user input.

## Live Demo

👉 👉 [Click here to try the app](https://learning-path-1.streamlit.app/)

## Working

Choose the required Topic, Learning Goal, adn the amount of time you can dedicate per day 
![image](https://github.com/user-attachments/assets/f0fd445c-fb89-42cb-a399-e3bf6d576163)


Then click on the "Generate My Learning Path" to get your learning path
![image](https://github.com/user-attachments/assets/fd57e4cd-6899-4fe5-b498-4bdc190fc38f)


## Installation

```bash
git clone https://github.com/Rajesh-M01/Learning-Path
cd Learning-Path
pip install -r requirements.txt
streamlit run app.py
