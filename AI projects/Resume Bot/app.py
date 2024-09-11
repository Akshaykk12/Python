import os
import streamlit as st
from templates import resumeTemplate
from uprofile import myProfile
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

def create_prompt(job_description):
    
    prompt = f"""
    I would like to generate a custom professional resume .

    ### My Profile:
    {myProfile}

    ### Job Description:
    {job_description}

    Based on the above information, please generate a resume in  that highlights my skills and qualifications, tailored to the job description provided.

    - Ensure the resume is formatted professionally.
    - Structure the resume to include sections like: Personal Information, Objective, Experience, Skills, Education, and Certifications.
    - Align the content from my profile with the job description, making it relevant and specific to the role.
    - Ensure the  properly formatted and includes any necessary packages or formatting settings.

    

    Please generate the resume using this template only. Mimic every little details. 
    
    """


    return prompt

def generate_latex_resume(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt, generation_config= genai.types.GenerationConfig(temperature=0.0))
    return response



st.title("Resume Bot")
job_description = st.text_area("Enter the job description", height = 260)

if job_description:
    prompt = create_prompt(job_description)
    latex_resume = generate_latex_resume(prompt)
    st.code(latex_resume)