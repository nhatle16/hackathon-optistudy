# OptiStudy AI — Project Overview & Feature Specification

## Core Concept
OptiStudy AI transforms unstructured academic syllabi and course materials into prioritized, dependency-aware study roadmaps constrained by student availability.

---

## Feature Specifications

### 1. Smart Syllabus Ingestion
Extracts core operational data and grading rubrics from uploaded course documents (PDFs, images, or documents) using multimodal vision models.
* **Grading Weight Parser:** Automatically maps percentage breakdowns across homework, labs, midterms, and finals.
  * *Example:* Ingests a 7-page PDF and immediately isolates that Midterm 1 covers 25% of the total grade across only three chapters.
  * *Example:* Flags that weekly lab attendance carries a strict 10% penalty threshold.
* **Support System Anchor:** Extracts TA office hours, tutorial sections, and help-desk channels.
  * *Example:* Pulls "Tues/Thurs 2–4 PM, Room 310" for the course TA and pairs it with upcoming assignment milestones.
  * *Example:* Detects discussion board links and instructor email response policies.

### 2. Dependency Mapping & Prerequisite Graph
Constructs a Directed Acyclic Graph (DAG) of the course concepts so students master foundational topics before tackling complex applications.
* **Prerequisite Chain Builder:** Orders study tasks by logical progression rather than naive chronological sequence.
  * *Example:* Enforces mastery of *Matrix Multiplication* before scheduling *Neural Network Forward Passes*.
  * *Example:* Links assignment prompts directly to the minimal set of lecture topics required to solve them.
* **Interactive Graph Visualizer:** A node-link diagram with clear state signaling:
  * **Slate (Locked / Unvisited):** Topics waiting on prerequisite completion.
  * **Amber (Needs Review):** Concepts flagged due to missed practice or low confidence.
  * **Emerald (Mastered):** Topics cleared through successful practice.

### 3. Triage Mode ("The Panic Button")
A one-click constrained optimizer designed for students with limited study windows (e.g., 2–4 hours before an exam).
* **Yield-Maximizing Knapsack Solver:** Filters out non-essential historical context and deep mathematical proofs, prioritizing high-yield concepts that maximize expected points per minute.
  * *Example:* With 2 hours remaining, cuts 40 pages of theoretical readings to focus strictly on 3 guaranteed exam question patterns.
  * *Example:* Generates an instant, exportable 1-page high-yield cheat sheet summarizing formulas and definitions.
* **Canonical Problem Drilling:** Focuses study time entirely on high-probability exam problems.
  * *Example:* Replaces generic passive flashcards with step-by-step walkthroughs of recurring midterm questions.

### 4. Adaptive Routing & Dynamic Calibration
Continuously customizes future study plans based on active mastery checks and personal velocity, avoiding passive star ratings and guilt-inducing failure screens.
* **Active Micro-Checkpoints:** Verifies retention with targeted, single-concept questions rather than subjective self-evaluations.
  * *Example:* Prompts: *"What happens to the gradient if weights are initialized to zero?"* If answered incorrectly, the system automatically inserts a 10-minute targeted review.
  * *Example:* Correct answers immediately mark the corresponding node emerald and unlock downstream topics.
* **Pacing Calibration Engine:** Tracks user reading and problem-solving speed against initial estimates.
  * *Example:* If practice problems take 1.5× the estimated time, future study blocks dynamically stretch their allocated buffers by 50%.
  * *Example:* Gathers post-exam schedule ratings to refine estimated topic difficulty for future study modules.
