import openai
import os

# Set the OpenAI API key
openai.api_key = "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"

def generate_interview_questions(job_requirements):
    """
    Generates a set of interview questions based on the given job requirements using the GPT-3 language model.
    Args:
        job_requirements (str): A string containing the job requirements.
    Returns:
        str: A string containing the generated interview questions.
    """

    # Use the ChatGPT model to generate text based on the job requirements
    prompt = (f"Generate 15-20 interview questions with answers for a job with the following requirements:\n{job_requirements}")
    completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=3000)
    interview_questions = completions.choices[0].text

    return interview_questions

job_requirements = "At least 1 to 2 years of experience in cloud infra/dev ops\n2+ years of experience in AWS/GCP/Azure\nExperience in Maven, Gradle, Grunt, Unix\nIdea of IaC tools like Terraform,Cloud formation or ARM templates\nExpertise in Docker and Kubernetes is a must\nProficiency in Linux, Shell scripting, Git\nIdea of cloud security"
interview_questions = generate_interview_questions(job_requirements)
print(interview_questions)