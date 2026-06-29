from utils.similarity import calculate_similarity


def get_ats_score (resume_text,job_discription):

    score = calculate_similarity(
        resume_text,
        job_discription
    )

    resume score