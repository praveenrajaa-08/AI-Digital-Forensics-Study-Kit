# Project Report: AI Digital Forensics Concepts Study Kit

## 1. Abstract
The AI Digital Forensics Concepts Study Kit is a learning-oriented web application that introduces digital forensics concepts. It includes study modules, a rule-based synthetic login-log analyzer, SHA-256 file hashing, and a knowledge quiz. The system is designed for beginner cybersecurity students and demonstrates how software can assist with evidence triage while keeping a human investigator responsible for conclusions.

## 2. Problem Statement
Digital forensics terminology and investigation workflows can be difficult for beginners. Students also need safe, practical demonstrations of evidence integrity and log review without accessing private or unauthorized data.

## 3. Objectives
- Present key digital forensics concepts in simple language.
- Demonstrate transparent triage rules on synthetic login logs.
- Calculate SHA-256 digests for selected test files.
- Assess learning through a quiz.
- Promote ethical, authorized evidence handling.

## 4. Scope
The project is an educational prototype. It does not acquire evidence from real devices, recover deleted files, identify individuals, or determine criminal responsibility. The login analyzer uses simple rules rather than a trained AI model.

## 5. Technologies
- Python: application logic and hashing.
- Streamlit: interactive web interface.
- pandas: CSV loading and analysis.
- hashlib: SHA-256 calculation.

## 6. System Modules
1. Study Modules
2. Sample Log Analyzer
3. File Integrity Checker
4. Knowledge Quiz

## 7. Methodology
The user selects a module or supplies a permitted test file. For log analysis, the application checks each record against visible rules and annotates records that may need review. For integrity checking, it calculates a SHA-256 digest. Quiz answers are checked against an answer key and explanations are shown.

## 8. Testing Plan
- Confirm the dashboard and study modules load.
- Load the bundled synthetic CSV and verify required columns.
- Check that records with five or more failed attempts are marked.
- Upload a test file and verify a 64-character hexadecimal SHA-256 digest.
- Submit quiz answers and confirm score and explanations.
- Test malformed CSV input and missing columns.

## 9. Limitations
- Rule-based log analysis is simplistic and may generate false positives or miss suspicious behavior.
- Hashing verifies content consistency only when compared with a trusted digest.
- The prototype is not a forensic acquisition or case-management system.
- No real-world accuracy claims are made.

## 10. Future Enhancements
- Add unit tests, timelines, and more log formats.
- Add an optional anomaly-detection model evaluated on suitable labeled data.
- Add an audit trail and report export.
- Improve accessibility and multilingual learning notes.

## 11. Conclusion
The project provides a safe introduction to digital forensics through educational content and small practical demonstrations. It emphasizes transparency, evidence integrity, privacy, and human validation.
