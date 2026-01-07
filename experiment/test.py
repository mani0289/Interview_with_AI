from src.mcqgen.mcqgenerator import interview_question_chain, interview_answer_chain

dummy_resume = """
I am a Data Engineer with 2.5 years of experience.
I have strong skills in Python, SQL, and AWS.
I recently worked on a migration project moving data to Snowflake.
"""

dummy_jd = """
We are looking for a Senior Data Engineer.
Must know Python, AWS Glue, and be able to optimize SQL queries.
Experience with Generative AI is a plus.
"""


print("Generating Interview Questions...")
questions = interview_question_chain.invoke({
    'resume': dummy_resume,
    'job_description': dummy_jd
})
print(questions)

print("\nGenerating Ideal Answers...")
answers = interview_answer_chain.invoke({
    'interview_questions': questions
})
print(answers)  