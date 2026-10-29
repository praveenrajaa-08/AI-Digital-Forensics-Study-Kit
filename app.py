import hashlib
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Digital Forensics Study Kit", page_icon="🔎", layout="wide")

DATA_DIR = Path(__file__).parent / "sample_data"

MODULES = {
    "Digital Forensics Basics": {
        "summary": "Digital forensics is the process of identifying, preserving, examining, and reporting digital evidence.",
        "points": [
            "Preserve original evidence and document every action.",
            "Work from a verified copy whenever possible.",
            "Maintain a clear chain of custody.",
            "Use repeatable methods and record tool versions.",
        ],
    },
    "Computer and Mobile Forensics": {
        "summary": "Computer forensics examines computers and storage media. Mobile forensics examines phones, tablets, and related data.",
        "points": [
            "Potential sources include files, metadata, application data, and system logs.",
            "Encryption and device locks can limit access.",
            "Collection must be authorized and privacy-aware.",
        ],
    },
    "Network Forensics": {
        "summary": "Network forensics examines network traffic and logs to understand events and potential incidents.",
        "points": [
            "Sources can include firewall, DNS, VPN, and server logs.",
            "A suspicious indicator is not automatically proof of malicious intent.",
            "Correlate timestamps and time zones carefully.",
        ],
    },
    "Evidence Integrity and Hashing": {
        "summary": "A cryptographic hash creates a fixed-length digest that can help verify whether a file has changed.",
        "points": [
            "SHA-256 is commonly used for integrity checks.",
            "Matching hashes support that two files have the same content.",
            "A hash alone does not prove who created a file or whether its contents are truthful.",
        ],
    },
    "AI in Digital Forensics": {
        "summary": "AI can help prioritize large datasets, identify unusual patterns, and summarize findings for human review.",
        "points": [
            "Models may produce false positives and false negatives.",
            "Keep explanations and source records available for review.",
            "A human investigator must validate important findings.",
        ],
    },
}

QUIZ = [
    ("What is the main purpose of a cryptographic hash in a forensic workflow?",
     ["To prove guilt", "To help check file integrity", "To recover every deleted file", "To identify a person automatically"], 1,
     "A hash helps compare file contents and detect changes; it does not prove guilt or identity."),
    ("What does chain of custody document?",
     ["The evidence handling history", "A computer's screen resolution", "The AI model's color theme", "The user's password"], 0,
     "Chain of custody records who handled evidence, when, and what was done."),
    ("An AI tool flags a login as suspicious. What should happen next?",
     ["Treat it as conclusive proof", "Delete the log", "Review the underlying evidence", "Publish the user's details"], 2,
     "AI flags are leads that require contextual human review."),
    ("Which algorithm is implemented in this project for file hashing?",
     ["MD5 only", "SHA-256", "RSA encryption", "Base64"], 1,
     "The file-integrity checker uses SHA-256 via Python hashlib."),
    ("Which dataset is safest for a classroom demonstration?",
     ["A stranger's private logs", "A leaked company database", "Synthetic sample logs", "A classmate's phone backup"], 2,
     "Use synthetic, authorized, or properly consented datasets."),
]

def sha256_file(uploaded_file):
    digest = hashlib.sha256()
    for chunk in iter(lambda: uploaded_file.read(1024 * 1024), b""):
        digest.update(chunk)
    uploaded_file.seek(0)
    return digest.hexdigest()

def classify_login(row):
    reasons = []
    try:
        failed = int(row.get("failed_attempts", 0))
    except (ValueError, TypeError):
        failed = 0
    status = str(row.get("status", "")).strip().lower()
    if failed >= 5:
        reasons.append("many failed attempts (5 or more)")
    if status == "failure":
        reasons.append("login result recorded as failure")
    if str(row.get("source_ip", "")).startswith(("198.51.100.", "203.0.113.", "192.0.2.")):
        reasons.append("documentation/example IP range")
    return "; ".join(reasons) if reasons else "No simple rule triggered"

st.title("🔎 AI Digital Forensics Concepts Study Kit")
st.caption("A beginner-friendly educational demo • Use only authorized or synthetic evidence")
st.warning("Educational use only. Findings are indicators for review, not proof of wrongdoing. Do not upload private or unauthorized evidence.")

pages = ["Overview", "Study Modules", "Sample Log Analyzer", "File Integrity Checker", "Knowledge Quiz"]
page = st.sidebar.radio("Navigate", pages)

if page == "Overview":
    st.subheader("Project overview")
    st.write("Learn digital forensics concepts and try safe demonstrations of log triage and file-integrity verification.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Study modules", len(MODULES))
    c2.metric("Quiz questions", len(QUIZ))
    c3.metric("Hash algorithm", "SHA-256")
    st.markdown("### Included features")
    st.markdown("- Concise study notes on digital forensics\n- Rule-based triage of synthetic login logs\n- SHA-256 file hashing\n- Short multiple-choice quiz with explanations")
    st.markdown("### Suggested workflow")
    st.markdown("1. Read a study module.\n2. Explore the included sample login dataset.\n3. Upload a harmless test file to calculate its SHA-256 hash.\n4. Complete the quiz.")
    st.info("This demo uses transparent rules for log triage rather than claiming to train a production AI model.")

elif page == "Study Modules":
    st.subheader("Study modules")
    chosen = st.selectbox("Choose a topic", list(MODULES.keys()))
    module = MODULES[chosen]
    st.markdown(f"### {chosen}")
    st.write(module["summary"])
    st.markdown("#### Key points")
    for point in module["points"]:
        st.markdown(f"- {point}")
    with st.expander("Mini revision question"):
        st.write("Why should investigators preserve evidence and document their actions?")
        st.write("Sample answer: To maintain integrity, support repeatability, and show how evidence was handled.")

elif page == "Sample Log Analyzer":
    st.subheader("Sample login-log analyzer")
    st.write("This transparent rule-based demo flags rows with five or more failed attempts or a failure status.")
    csv_path = DATA_DIR / "login_logs.csv"
    try:
        sample_df = pd.read_csv(csv_path)
    except Exception as exc:
        st.error(f"Could not read sample dataset: {exc}")
        st.stop()
    uploaded = st.file_uploader("Optional: upload an authorized CSV with timestamp, username, source_ip, status, failed_attempts", type=["csv"])
    if uploaded:
        try:
            df = pd.read_csv(uploaded)
        except Exception as exc:
            st.error(f"Could not read CSV: {exc}")
            st.stop()
    else:
        df = sample_df
        st.caption("Showing the bundled synthetic sample dataset.")
    required = {"timestamp", "username", "source_ip", "status", "failed_attempts"}
    missing = required - set(df.columns)
    if missing:
        st.error("Missing required columns: " + ", ".join(sorted(missing)))
    else:
        df = df.copy()
        df["review_reason"] = df.apply(classify_login, axis=1)
        df["needs_review"] = df["review_reason"] != "No simple rule triggered"
        st.metric("Rows marked for review", int(df["needs_review"].sum()))
        st.dataframe(df, use_container_width=True)
        st.download_button("Download annotated CSV", df.to_csv(index=False).encode("utf-8"), "annotated_login_logs.csv", "text/csv")
        st.caption("The example IP ranges are reserved for documentation. All bundled records are synthetic.")

elif page == "File Integrity Checker":
    st.subheader("SHA-256 file integrity checker")
    st.write("Choose a file to calculate its SHA-256 digest. The file is processed in this session and is not saved by this app.")
    uploaded_file = st.file_uploader("Choose a test file", type=None)
    if uploaded_file:
        digest = sha256_file(uploaded_file)
        st.success("SHA-256 digest calculated.")
        st.code(digest)
        st.download_button("Download hash record", f"Filename: {uploaded_file.name}\nSHA-256: {digest}\n", "hash_record.txt", "text/plain")
        st.caption("Compare hashes from trusted points in the workflow. A matching hash supports content integrity but does not establish authenticity by itself.")

elif page == "Knowledge Quiz":
    st.subheader("Knowledge quiz")
    with st.form("quiz_form"):
        answers = []
        for i, (question, options, correct, explanation) in enumerate(QUIZ):
            st.markdown(f"**{i+1}. {question}**")
            answers.append(st.radio("Select one answer", options, key=f"q{i}", index=None, label_visibility="collapsed"))
        submitted = st.form_submit_button("Check answers")
    if submitted:
        score = 0
        for i, answer in enumerate(answers):
            question, options, correct, explanation = QUIZ[i]
            if answer == options[correct]:
                score += 1
                st.success(f"{i+1}. Correct — {explanation}")
            else:
                st.error(f"{i+1}. Review — {explanation}")
        st.metric("Your score", f"{score} / {len(QUIZ)}")
        st.write("Review the study modules for any concepts you missed.")

st.sidebar.markdown("---")
st.sidebar.caption("Student project • Python + Streamlit + pandas")
