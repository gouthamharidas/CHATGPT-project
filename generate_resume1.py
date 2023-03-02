import openai

# Set the OpenAI API key
openai.api_key = "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"

def generate_resume_text(job_requirements, Name, Email_id, Work_experience, Education, Phone_number):
    """
    Generates a resume based on the given job requirements using the ChatGPT language model.
    Args:
        job_requirements (str): A string containing the job requirements.
    Returns:
        str: A string containing the generated resume.
    """
    # Use the ChatGPT model to generate text based on the job requirements
    prompt = (f"Please create an expertly crafted professional resume for me that showcases my IT expertise. The resume should include the following personal details: Name, Email, Phone Number. Additionally, I need a Professional Summary that highlights my skills and experience, a comprehensive Education section, and a Work Experience section that outlines my past roles and responsibilities (INCLUDE 5-7 RESPONSIBILITIES FOR EACH PROJECT). I would like to highlight two projects I have worked on, including my role and the tasks I accomplished. Please take the following inputs as reference: {job_requirements}, {Name}, {Email_id}, {Work_experience}, {Education}, {Phone_number}. The format should be professional and appealing to potential employers in the IT field.")   
    completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=3600)
    resume = completions.choices[0].text

    return resume


