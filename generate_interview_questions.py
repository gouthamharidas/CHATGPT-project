import openai


# Set the OpenAI API key
openai.api_key = "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"

def generate_interview_questions(job_requirements):
    """
    Generates interview questions based on the given job requirements using the ChatGPT language model.
    Args:
        job_requirements (str): A string containing the job requirements.
    Returns:
        str: A string containing the generated interview questions.
    """
    # Use the ChatGPT model to generate text based on the job requirements
    prompt = (f"Write 30 technical interview questions for a job based on the :{job_requirements} starting with 1.")
    completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=3000)
    interview_questions = completions.choices[0].text

    questions = interview_questions.split("\n")
     


    return questions
