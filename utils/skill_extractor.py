skills_database = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "react",
    "javascript",
    "nodejs"
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "scikit-learn",
    "opencv",
    "steamlit",
    "flask",
    "fastapi",
    "git",
    "github",
    "docker",
    "aws",
    "power bi",
    "excel"

]

def extarct_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_database:

        if skill.lower() in text:

            found_skills.append(skill)

    return sorted(list(set(found_skills)))