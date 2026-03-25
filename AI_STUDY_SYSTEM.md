# AI Study System

This file turns the roadmap into a repeatable learning process.

## Goal

Use AI to improve understanding, discipline, and feedback without letting it do the thinking for you.

## Core Rule

The order is:
1. Read
2. Think
3. Write your own explanation
4. Ask AI for correction or expansion
5. Implement
6. Review mistakes

If AI comes before your own attempt, you learn less.

## AI Roles

### 1. Tutor
Use when:
- a concept feels abstract
- the math is unclear
- you need multiple explanations

Prompt pattern:

```text
Act as a rigorous AI tutor.
Topic: <topic>
My current level: <beginner/intermediate>
What I already understand: <your notes>
What confuses me: <specific gap>

Teach this in 3 layers:
1. Intuition
2. Math
3. Small Python example

Then ask me 3 questions to check understanding.
```

### 2. Reviewer
Use when:
- you finished reading a topic
- you want to test whether you actually understand it

Prompt pattern:

```text
Act as a strict reviewer.
I studied: <topic>

Quiz me with:
1. 3 conceptual questions
2. 2 mathematical questions
3. 1 implementation question

Do not give the answers immediately.
After I answer, grade me, identify weak areas, and tell me what to revise next.
```

### 3. Coach
Use when:
- you feel lost
- a topic is too large
- you need a weekly plan

Prompt pattern:

```text
Act as a learning coach for AI and data science.
My current phase: <math/ml/deep learning/applied/advanced>
Time available per day: <time>
Days per week: <number>
Current strengths: <topics>
Current weaknesses: <topics>

Create a 7-day study plan with:
- one main goal
- daily tasks
- one checkpoint
- one mini implementation task
- one review session
```

### 4. Project Mentor
Use when:
- you need practice beyond theory
- you want a mini-project that matches your current level

Prompt pattern:

```text
Act as a project mentor.
I am studying: <topic>
My current level: <level>

Design one mini-project that forces me to use this topic.
Include:
- project goal
- required concepts
- dataset or input idea
- implementation steps
- common mistakes
- evaluation checklist
```

## Session Workflow

Use this in each study session.

### Step 1. Define the target
Write:
- topic
- why it matters
- what “done” means for today

Good examples:
- Understand gradient descent update rule
- Derive logistic regression loss
- Implement matrix multiplication without NumPy

### Step 2. Make your own attempt first
Before opening AI, write:
- your current explanation
- formulas you remember
- where you are confused

### Step 3. Use AI narrowly
Ask for help on one problem at a time:
- explanation
- derivation
- debugging
- exercise generation

Avoid broad prompts like “teach me everything about deep learning” during a normal session.

### Step 4. Produce an artifact
Every session should end with one artifact:
- notes
- solved exercise
- derivation
- code file
- short summary

### Step 5. Close the loop
Finish by answering:
- What did I understand today?
- What still feels weak?
- What is the next exact task?

## Weekly Review Workflow

At the end of each week:
1. list what you studied
2. list what you implemented
3. list what you still cannot explain clearly
4. ask AI to rank your weak areas
5. plan the next week around the top 1 to 2 gaps

## Quality Bar

Do not mark a topic as done unless you can do most of these:
- explain it simply
- derive key parts without copying
- implement a basic version
- solve one related problem
- connect it to a real ML or DS use case

## Anti-Patterns

Avoid these habits:
- reading passively without output
- copying AI answers into notes without understanding
- jumping topics too early
- using frameworks before understanding the core idea
- studying only theory with no code

## Minimal Weekly Cadence

If time is limited, use this baseline:
- 4 study sessions per week
- 60 to 90 minutes per session
- 1 review session per week
- 1 small implementation every week

## First Practical Setup

Use this repository like this:
- keep roadmap and planning in the root docs
- store session logs in a journal folder
- store notes by topic
- store small exercises and experiments in topic folders
- use the templates folder to standardize your process