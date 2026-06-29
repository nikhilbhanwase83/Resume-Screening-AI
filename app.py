import streamlit as st

from utils.pdf_reader import extract_pdf_text
from utils.docx_reader import extract_docx_text
from utils.parser import (
    extract_name,
    extract_email,
    extract_phone,
    extract_education,
    extract_experience,
)

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Resume Screening AI",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------

st.title("📄 Resume Screening AI")
st.subheader("ATS Score Analyzer using NLP")

st.write("Upload your resume and compare it with a Job Description.")

st.markdown("---")

# -----------------------------
# Upload Resume
# -----------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Resume",
    type=["pdf", "docx"]
)

# -----------------------------
# Job Description
# -----------------------------

job_description = st.text_area(
    "📝 Paste Job Description",
    height=200,
    placeholder="Paste the complete job description here..."
)

st.markdown("")

# -----------------------------
# Analyze Button
# -----------------------------

if st.button("🚀 Analyze Resume", use_container_width=True):

    # -----------------------------
    # Validation
    # -----------------------------

    if uploaded_file is None:

        st.warning("Please upload a Resume.")

    elif job_description.strip() == "":

        st.warning("Please paste a Job Description.")

    else:

        # -----------------------------
        # Read Resume
        # -----------------------------

        if uploaded_file.type == "application/pdf":

            resume_text = extract_pdf_text(uploaded_file)

        else:

            resume_text = extract_docx_text(uploaded_file)

        # -----------------------------
        # Candidate Details
        # -----------------------------

        name = extract_name(resume_text)

        email = extract_email(resume_text)

        phone = extract_phone(resume_text)

        education = extract_education(resume_text)

        experience = extract_experience(resume_text)

        # -----------------------------
        # Success
        # -----------------------------

        st.success("Resume analyzed successfully!")

        # -----------------------------
        # Metrics
        # -----------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Resume", "Uploaded")

        with col2:
            st.metric("Status", "Success")

        with col3:
            st.metric("Experience", experience)

        st.markdown("---")

        # -----------------------------
        # Candidate Information
        # -----------------------------

        st.subheader("👤 Candidate Information")

        c1, c2 = st.columns(2)

        with c1:

            st.write("### Name")
            st.success(name)

            st.write("### Email")
            st.info(email)

            st.write("### Phone")
            st.info(phone)

        with c2:

            st.write("### Education")

            if education:
                st.success(", ".join(education))
            else:
                st.warning("Not Found")

            st.write("### Experience")
            st.success(experience)

        st.markdown("---")

        # -----------------------------
        # Resume Text
        # -----------------------------

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=350
        )

        st.markdown("---")

        # -----------------------------
        # Job Description
        # -----------------------------

        st.subheader("📝 Job Description")

        st.text_area(
            "Job Description",
            job_description,
            height=250
        )

        st.markdown("---")

        # -----------------------------
        # Next Module
        # -----------------------------

        st.info("✅ Next Step: Skill Extraction")

        st.info("✅ ATS Score Module")

        st.info("✅ Missing Skills")

        st.info("✅ AI Recommendations")

        st.info("✅ Dashboard Charts")