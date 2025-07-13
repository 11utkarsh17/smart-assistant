import streamlit as st
from summarizer import generate_summary
from question_gen import generate_challenge_questions, evaluate_answer
from logic import extract_text_from_pdf, extract_text_from_txt

st.set_page_config(page_title="Smart Research Assistant", layout="centered")
st.title("📘 Smart Research Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        document_text = extract_text_from_pdf(uploaded_file)
    else:
        document_text = extract_text_from_txt(uploaded_file)

    st.subheader("🧠 Auto Summary")
    summary = generate_summary(document_text)
    st.info(summary)

    mode = st.radio("Choose Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        user_query = st.text_input("Ask a question based on the document:")
        user_answer = st.text_input("Your Answer:")
        if user_query and user_answer:
            response = evaluate_answer(document_text, user_query, user_answer)
            st.success(response)
        elif user_query or user_answer:
            st.warning("⚠️ Please fill both the question and answer fields.")

    elif mode == "Challenge Me":
        questions_text = generate_challenge_questions(document_text)
        questions = questions_text.strip().split("\n")
        st.markdown("### 🧠 Challenge Questions")

        for i, q in enumerate(questions):
            if q.strip():
                st.markdown(f"**Q{i+1}. {q.strip()}**")
                user_ans = st.text_input(f"Your Answer to Q{i+1}")
                if user_ans:
                    feedback = evaluate_answer(document_text, q.strip(), user_ans)
                    st.info(feedback)
