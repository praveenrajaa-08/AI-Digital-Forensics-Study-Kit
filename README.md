# AI Digital Forensics Concepts Study Kit

A beginner-friendly cybersecurity mini-project for learning digital forensics concepts through study notes, synthetic login-log triage, SHA-256 file hashing, and a short quiz.

## Features

- **Study modules:** digital forensics basics, computer/mobile forensics, network forensics, evidence integrity, and AI in forensics.
- **Sample log analyzer:** applies transparent rules to synthetic login records and marks entries for human review.
- **File integrity checker:** calculates SHA-256 for a file selected by the user.
- **Knowledge quiz:** multiple-choice questions with explanations.
- **CSV export:** download annotated sample-log results.

> **Responsible use:** This is an educational demonstration, not a production forensic tool. Use only synthetic, authorized, or properly consented data. A flagged record is not proof of wrongdoing. Do not upload private or unauthorized evidence.

## Requirements

- Python 3.10 or newer recommended
- pip

## Run locally

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment (recommended).

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app should open in your browser. If it does not, use the local URL shown in the terminal.

## Sample CSV format

The analyzer expects these columns:

- `timestamp`
- `username`
- `source_ip`
- `status`
- `failed_attempts`

The bundled `sample_data/login_logs.csv` contains synthetic demonstration data. You can upload a CSV only when you are authorized to analyze it.

## How it works

1. Read a selected learning module.
2. Inspect the synthetic login log and review rule-triggered records.
3. Select a test file to calculate its SHA-256 hash.
4. Take the quiz and read explanations.

The log analyzer is rule-based and explainable; it does not claim to train a machine-learning model. This keeps the demo transparent and easy to extend for a student project.

## Project structure

```text
ai-digital-forensics-study-kit/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── sample_data/
    └── login_logs.csv
```

## Possible future improvements

- Add authorized sample datasets and additional parsers.
- Add time-zone normalization and visual timelines.
- Add a clearly evaluated anomaly-detection model.
- Add unit tests and evidence-handling audit logs.
- Add exportable investigation reports.

## Academic project note

Suggested title: **AI Digital Forensics Concepts Study Kit**  
Suggested category: **Cybersecurity / Digital Forensics / Educational Tool**

Customize this repository with your own project screenshots, test results, and report before submission.
