import streamlit as st
import pandas as pd
from src.mcqgen.mcqgenerator import interview_question_chain, interview_answer_chain
from src.mcqgen.utils import get_pdf_text,docx
from src.mcqgen.logger import logger

##Page Configuration
st.set_page_config(page_title="AI Interview Coach",page_icon="🎓")
st.title("🤖 GenAI Interview Prep Assistant")
st.markdown("Bridge the gap between your resume and your dream job.")

##Sidebar for Inputs
with st.sidebar:
    st.header("Upload Documents")
    uploaded_file = st.file_uploader("Upload your Resume (PDF or TEXT OR DOCX)", type=["pdf","txt","docx"])
    job_description = st.text_area("Paste the Job Description (JD) here:", height=300)


if st.button("Generate Interview Prep"):
    if uploaded_file and job_description:
        with st.spinner("Analyzing your profile and the job requirements..."):
            # 1. Extract Resume Text
            logger.info(f"New resume uploaded:{uploaded_file.name}")
            resume = get_pdf_text(uploaded_file)
            
            # 2. Run Chain 1 (Generate Questions)
            questions = interview_question_chain.invoke({
                "resume": resume,
                "job_description": job_description
            })
            
            # 3. Run Chain 2 (Get Answers)
            answers = interview_answer_chain.invoke({"interview_questions": questions})
            
            # 4. Display Results
            df=pd.DataFrame(answers)

            st.divider()
            st.header("🎯 Your Personalized Interview Prep")
            st.subheader("📊 Questions Table:")
            st.table(df[["question","ideal_answer"]])
            st.subheader("📝 Detailed Questions & Answers:")
            for index,row in df.iterrows():
                with st.expander(f"Question{index+1}:{row['question']}"):
                    st.write(f"**Ideal Answer:**{row['ideal_answer']}")
    
        ##Add a Download Button (The "Job-Ready" touch)
        report_lines = ["INTERVIEW PREP REPORT\n" + "="*30 + "\n"]

        for index, row in df.iterrows():
            report_lines.append(f"\nQ {index+1}: {row['question']}\n")
            report_lines.append(f"A: {row['ideal_answer']}\n")
            report_lines.append("-"*20 + "\n")

        full_report_text = "\n".join(report_lines)

        st.download_button(
            label="Download Prep Material as TXT",
            data=full_report_text,
            file_name="interview_prep.txt",
            mime="text/plain"
        )
    else:
        st.error("Please upload your Resume and provide the Job Description to proceed.")
