import os
import streamlit as st
from templates import resumeTemplate
from uprofile import myProfile
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
# import easyocr
# import numpy as np
# from PIL import Image
# from pdf2image import convert_from_bytes
from pypdf import PdfReader


genai.configure(api_key=os.getenv("API_KEY"))
# reader = easyocr.Reader(["en"])

def create_prompt(job_description, profile):

    upgraded_prompt = f"""
    You are an expert latex resume writer with over 20 years of experienceworking with job seekers trying to land a role in tech.
    Highlight the 3 most important responsibilities in this job description:
    {job_description}
    Based on these 3 most important responsibiities from job description, please tailor a Latex resume for this role. Do not make information up. Here's my resume:
    {profile}
    Please use this latex resume for reference:
    {resumeTemplate}
    And accordingly give me code of that Latex resume. It should be one page Latex resume, so arrange elements horizontally wherever required to save up space.
    Don't give any explaination at the end, just a latex code. Based on these 3 most important responsibiities from job description, please tailor a Latex resume for this role.
    """
    
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
    -    Ensure the  properly formatted and includes any necessary packages or formatting settings.

    

    Please generate the resume using this template only. Mimic every little details. You can order the arrangement of the sections such that it matches with the job. Make sure that the Latex code is sufficient for one page resume.
    Make sure you use "textbf" for bolding the texts. And use margin of only 2cm.
    Give me Latex code such that Name(At top of resume Big and bold) and contact details will be at the top of the resume. Contact information will be  organized horizontally. Dont add any fake information like work experience and dont write objective but instead use summary there.
    
    """


    return upgraded_prompt

def generate_latex_resume(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt, safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    })
    return response.text

# def perform_ocr(image):
#     image_np = np.array(image)
#     results = reader.readtext(image_np)
#     text = " ".join(result[1] for result in results)
#     return text

def read_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    page = reader.pages[0]

    text = page.extract_text()
    return text
#     pdf = PDFQuery(uploaded_file)
#     pdf.load()
#     text_elements = pdf.pq("LTTextLineHorizontal")
#     text = [t.text for t in text_elements]
#     return text


st.title("Resume Bot")
job_description = st.text_area("Enter the job description", height = 260)
uploaded_file = st.file_uploader("Upload your Resume", type=["pdf"])

if st.button("Generate Resume"):

    text = read_pdf(uploaded_file)
    prompt = create_prompt(job_description, text)
    latex_resume = generate_latex_resume(prompt)
    st.code(latex_resume)
        