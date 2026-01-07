from setuptools import find_packages, setup

setup(
    name='interview_generator',
    version='0.0.1',
    author='Manikanta Bandari',
    author_email='manikantabandari4@gmail.com',
    install_requires=["langchain", "langchain-google-genai", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)