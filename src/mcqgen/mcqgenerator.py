import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", api_key=key, temperature=0.3)

TEMPLATE = """
You are an expert Technical interviewer with 10 years of experience. I'll provide you with a candidate's resume and a job description. 

Your goal is to generate 5 targeted interview questions that test the gap between the resume and the JD.
Make sure to include:
1. Two technical questions on Python/SQL/AWS (based on the JD).
2. Two scenario-based questions on Data Pipelines (based on the Resume).
3. One behavioral question.

resume:{resume}

job_description:{job_description}

OUTPUT FORMAT:
Return ONLY the 5 questions as a numbered list. Do not add introductory text.
"""

prompt_gen_temp = PromptTemplate(
    input_variables=['resume','job_description'],
    template=TEMPLATE
)

interview_question_chain = prompt_gen_temp | llm | StrOutputParser()

TEMPLATE_ANSWER = """
You are an expert Career Coach.
Here are 5 interview questions generated for a candidate:
{interview_questions}

Please provide the "Ideal Answer" for each question.
Explain what the interviewer is looking for in a hidden "Interviewer's Note" for each.

OUTPUT FORMAT:
Return the result as a JSON object with keys "question", "ideal_answer", and "tip".
"""

answer_gen_temp = PromptTemplate(
    input_variables=['interview_questions'],
    template=TEMPLATE_ANSWER
)

interview_answer_chain = answer_gen_temp | llm | JsonOutputParser()