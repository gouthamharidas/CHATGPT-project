import openai


# Set the OpenAI API key
openai.api_key = "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"

def generate_cover_letter(job_requirements, resume_keywords):
    """
    Generates a cover letter based on the given job requirements using the ChatGPT language model.
    Args:
        job_requirements (str): A string containing the job requirements.
    Returns:
        str: A string containing the generated cover letter.
    """
    # Use the ChatGPT model to generate text based on the job requirements
    prompt = (f"Write an entended cover letter for a job with the following requirements:\n{job_requirements}\n\nMy resume highlights the following skills: {resume_keywords}, start with dear hiring manager")
    completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=3050)
    cover_letter = completions.choices[0].text

    return cover_letter
