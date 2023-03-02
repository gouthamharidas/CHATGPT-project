import openai
from flask import request


openai.api_key = "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"

    # rest of the function implementation
"""
    Generates a resume based on the given job requirements using the ChatGPT language model.
    Args:
        job_requirements (str): A string containing the job requirements.
    Returns:
        str: A string containing the generated resume.
    """
    # Use the ChatGPT model to generate text based on the job requirements

            
def analyze_job_fit1(job_requirements, resume_keywords, work_experience):
    prompt = (f"As an expert job analyst, please evaluate the alignment between the job requirements ({job_requirements}) and your combination of work experience ({work_experience}) and skills listed in your resume ({resume_keywords}). Take into account the significance and relevance of each job requirement, the connection between your experience and skills and the job requirements, and the relationship of your work experience to the job. Based on your analysis, provide a percentage that accurately reflects your suitability for the job opportunity and suggest any necessary changes to improve your fit for the role. Write the output in the second-person perspective.")
    completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=3050)
    analysis = completions.choices[0].text
    return analysis
