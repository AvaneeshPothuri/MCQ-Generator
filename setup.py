from setuptools import find_packages,setup
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Avaneesh Pothuri',
    author_email='pothuriavaneesh@gmail.com',
    install_reuires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)