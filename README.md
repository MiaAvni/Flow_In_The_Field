# Flow in the Field – Data Processing Challenge

This project is my solution to the **Sandbox Spring 2026 Caterpillar Challenge**, based on the *Flow in the Field* language-learning experiment. The goal of the application is to process participant, session, and round data retrieved from an API and compute meaningful statistics related to participant performance and engagement across languages.

---

## 📌 Problem Overview

Each participant in *Flow in the Field* plays one or more sessions of a language-learning matching game. Each session contains multiple rounds, and both sessions and rounds have timestamps and scores.

Given JSON data describing:
- participants
- sessions
- rounds  

The program computes per-participant statistics, including:
- average round score
- average session duration
- per-language statistics (average score and average round duration)

The final output is:
- sorted alphabetically by participant name
- formatted as JSON
- POSTed back to the same API endpoint

---

## 🧠 Design & Thought Process

I approached this problem by breaking it into clear stages:

1. **Data ingestion**
   - Fetch raw JSON data from the API using an HTTP GET request
   - Parse participants, sessions, and rounds into structured in-memory representations

2. **Data relationships**
   - Map sessions to participants
   - Map rounds to sessions
   - Group rounds by language per participant

3. **Computation**
   - Compute round durations and session durations using timestamps
   - Aggregate scores and durations
   - Handle edge cases (participants with zero sessions/rounds)

4. **Output formatting**
   - Round all numeric values to two decimal places
   - Sort participants alphabetically by name
   - Sort languages by total score (descending) per participant
   - Convert results back into valid JSON for POST submission

---

## ⚙️ How to Run the Project

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/flow-in-the-field.git
   cd flow-in-the-field
2. Run:
   ```bash
   python main.py
