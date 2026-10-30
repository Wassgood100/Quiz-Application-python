
import tkinter as tk
from tkinter import ttk, messagebox

# ======================================
# 1. QUIZ QUESTIONS
# ======================================

questions = [
    {
        "question": "Which markup language is used to structure web pages?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["input()", "print()", "show()", "display()"],
        "answer": "print()"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "Boolean"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "&"],
        "answer": "#"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["*", "**", "//", "%"],
        "answer": "**"
    },
    {
        "question": "Which Python data structure stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "question": "What does the len() function return?",
        "options": [
            "Number of items",
            "Data type",
            "Memory address",
            "Largest value"
        ],
        "answer": "Number of items"
    },
    {
        "question": "Which loop is commonly used to iterate through a sequence?",
        "options": ["if loop", "for loop", "switch loop", "def loop"],
        "answer": "for loop"
    },
    {
        "question": "Which keyword terminates the current loop?",
        "options": ["stop", "exit", "break", "continue"],
        "answer": "break"
    }
]


# ======================================
# 2. APPLICATION VARIABLES
# ======================================

current_question = 0
score = 0
answered = False

# Application colours
BG = "#F5F3FF"
PURPLE = "#6C4CE4"
DARK = "#24243A"
WHITE = "#FFFFFF"
GREEN = "#16A36A"
RED = "#DC4545"
GRAY = "#85859A"


# ======================================
# 3. MAIN WINDOW
# ======================================

root = tk.Tk()

root.title("Quiz Master - Python Quiz Application")
root.geometry("780x680")
root.minsize(700, 620)
root.configure(bg=BG)


# Progress bar style
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Quiz.Horizontal.TProgressbar",
    troughcolor="#E7E3F2",
    background=PURPLE,
    thickness=12
)


# ======================================
# 4. QUIZ FUNCTIONS
# ======================================

def start_quiz():

    global current_question, score, answered

    current_question = 0
    score = 0
    answered = False

    welcome_frame.pack_forget()
    result_frame.pack_forget()

    quiz_frame.pack(fill="both", expand=True)

    load_question()


def load_question():

    global answered

    answered = False

    data = questions[current_question]

    # Update question number
    question_number_label.config(
        text=f"QUESTION {current_question + 1} OF {len(questions)}"
    )

    # Display question
    question_label.config(
        text=data["question"]
    )

    # Reset selected answer
    selected_answer.set("")

    # Display answer options
    for i, option in enumerate(data["options"]):

        option_buttons[i].config(
            text=f"{chr(65 + i)}.   {option}",
            value=option,
            state="normal"
        )

    # Reset feedback
    feedback_label.config(
        text="Choose your answer below.",
        fg=GRAY
    )

    # Update score
    score_label.config(
        text=f"YOUR SCORE: {score}"
    )

    # Update progress bar
    progress_bar["value"] = current_question

    percentage = int(
        (current_question / len(questions)) * 100
    )

    progress_text.config(
        text=f"{percentage}% COMPLETED"
    )

    # Configure buttons
    check_button.config(state="normal")

    next_button.config(
        state="disabled",
        text="VIEW RESULTS" if current_question == len(questions) - 1
        else "NEXT QUESTION  →"
    )


def check_answer():

    global score, answered

    if answered:
        return

    answer = selected_answer.get()

    # Check if an option has been selected
    if answer == "":

        messagebox.showwarning(
            "No Answer Selected",
            "Please select an answer first!"
        )

        return

    correct_answer = questions[current_question]["answer"]

    # Compare selected answer with correct answer
    if answer == correct_answer:

        score += 1

        feedback_label.config(
            text="✓ Correct! Excellent work!",
            fg=GREEN
        )

    else:

        feedback_label.config(
            text=f"✗ Incorrect! Correct answer: {correct_answer}",
            fg=RED
        )

    answered = True

    # Disable answers after submission
    for button in option_buttons:
        button.config(state="disabled")

    # Update score
    score_label.config(
        text=f"YOUR SCORE: {score}"
    )

    # Update progress
    progress_bar["value"] = current_question + 1

    percentage = int(
        ((current_question + 1) / len(questions)) * 100
    )

    progress_text.config(
        text=f"{percentage}% COMPLETED"
    )

    # Disable Check Answer
    check_button.config(state="disabled")

    # Enable Next Question
    next_button.config(state="normal")


def next_question():

    global current_question

    if not answered:
        return

    # Move to next question
    if current_question < len(questions) - 1:

        current_question += 1

        load_question()

    else:

        show_results()


def show_results():

    quiz_frame.pack_forget()

    total_questions = len(questions)

    # Calculate final percentage
    percentage = (score / total_questions) * 100

    # Performance message
    if percentage >= 80:
        message = "Excellent Performance!"

    elif percentage >= 50:
        message = "Good Effort!"

    else:
        message = "Keep Practising!"

    # Display final results
    result_message.config(
        text=message
    )

    result_score.config(
        text=f"{score} / {total_questions}"
    )

    result_percentage.config(
        text=f"Your final percentage: {percentage:.1f}%"
    )

    result_frame.pack(fill="both", expand=True)


def restart_quiz():

    start_quiz()


def exit_application():

    root.destroy()


# ======================================
# 5. WELCOME SCREEN
# ======================================

welcome_frame = tk.Frame(
    root,
    bg=BG
)

welcome_frame.pack(
    fill="both",
    expand=True
)

tk.Label(
    welcome_frame,
    text="QUIZ MASTER",
    font=("Arial", 32, "bold"),
    fg=PURPLE,
    bg=BG
).pack(pady=(110, 15))

tk.Label(
    welcome_frame,
    text="Challenge your knowledge!",
    font=("Arial", 16),
    fg=DARK,
    bg=BG
).pack(pady=10)

tk.Label(
    welcome_frame,
    text="10 Questions  |  Multiple Choice  |  1 Mark Each",
    font=("Arial", 11),
    fg=GRAY,
    bg=BG
).pack(pady=15)

tk.Button(
    welcome_frame,
    text="START QUIZ",
    font=("Arial", 13, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground="#5234C1",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    width=22,
    height=2,
    command=start_quiz
).pack(pady=30)

tk.Button(
    welcome_frame,
    text="EXIT APPLICATION",
    font=("Arial", 10),
    bg=BG,
    fg=GRAY,
    relief="flat",
    cursor="hand2",
    command=exit_application
).pack()


# ======================================
# 6. QUIZ SCREEN
# ======================================

quiz_frame = tk.Frame(
    root,
    bg=BG
)


# Header
header = tk.Frame(
    quiz_frame,
    bg=BG
)

header.pack(
    fill="x",
    padx=35,
    pady=(25, 10)
)

tk.Label(
    header,
    text="QUIZ MASTER",
    font=("Arial", 20, "bold"),
    fg=PURPLE,
    bg=BG
).pack(side="left")


score_label = tk.Label(
    header,
    text="YOUR SCORE: 0",
    font=("Arial", 11, "bold"),
    fg=PURPLE,
    bg="#E9E4FF",
    padx=15,
    pady=10
)

score_label.pack(side="right")


# Progress section
progress_section = tk.Frame(
    quiz_frame,
    bg=BG
)

progress_section.pack(
    fill="x",
    padx=40,
    pady=15
)


question_number_label = tk.Label(
    progress_section,
    text="QUESTION 1 OF 10",
    font=("Arial", 10, "bold"),
    fg=DARK,
    bg=BG
)

question_number_label.pack(side="left")


progress_text = tk.Label(
    progress_section,
    text="0% COMPLETED",
    font=("Arial", 10, "bold"),
    fg=PURPLE,
    bg=BG
)

progress_text.pack(side="right")


# Progress bar
progress_bar = ttk.Progressbar(
    quiz_frame,
    style="Quiz.Horizontal.TProgressbar",
    maximum=len(questions),
    length=680,
    mode="determinate"
)

progress_bar.pack(
    padx=40,
    pady=5,
    fill="x"
)


# Question card
question_card = tk.Frame(
    quiz_frame,
    bg=WHITE,
    highlightbackground="#E4DFF0",
    highlightthickness=1
)

question_card.pack(
    fill="x",
    padx=40,
    pady=22
)


tk.Label(
    question_card,
    text="YOUR QUESTION",
    font=("Arial", 10, "bold"),
    fg=PURPLE,
    bg=WHITE
).pack(
    anchor="w",
    padx=25,
    pady=(20, 10)
)


question_label = tk.Label(
    question_card,
    text="",
    font=("Arial", 17, "bold"),
    fg=DARK,
    bg=WHITE,
    wraplength=620,
    justify="left"
)

question_label.pack(
    anchor="w",
    padx=25,
    pady=(5, 25)
)


# Answer options
options_frame = tk.Frame(
    quiz_frame,
    bg=BG
)

options_frame.pack(
    fill="x",
    padx=35,
    pady=5
)


selected_answer = tk.StringVar()

option_buttons = []

for i in range(4):

    button = tk.Radiobutton(
        options_frame,
        text="",
        variable=selected_answer,
        value="",
        font=("Arial", 12),
        bg=WHITE,
        fg=DARK,
        activebackground="#F0EDFF",
        selectcolor="#E9E4FF",
        indicatoron=False,
        relief="solid",
        bd=1,
        cursor="hand2",
        anchor="w",
        padx=20,
        pady=15
    )

    button.grid(
        row=i // 2,
        column=i % 2,
        padx=8,
        pady=8,
        sticky="ew"
    )

    option_buttons.append(button)


options_frame.grid_columnconfigure(0, weight=1)
options_frame.grid_columnconfigure(1, weight=1)


# Feedback label
feedback_label = tk.Label(
    quiz_frame,
    text="Choose your answer below.",
    font=("Arial", 11, "bold"),
    bg=BG,
    fg=GRAY
)

feedback_label.pack(pady=12)


# Button section
button_frame = tk.Frame(
    quiz_frame,
    bg=BG
)

button_frame.pack(pady=15)


# Check Answer button
check_button = tk.Button(
    button_frame,
    text="CHECK ANSWER",
    font=("Arial", 11, "bold"),
    bg="#E8E2FF",
    fg=PURPLE,
    activebackground="#D9D0FF",
    relief="flat",
    cursor="hand2",
    width=19,
    height=2,
    command=check_answer
)

check_button.grid(
    row=0,
    column=0,
    padx=10
)


# Next Question button
next_button = tk.Button(
    button_frame,
    text="NEXT QUESTION  →",
    font=("Arial", 11, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground="#5234C1",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    width=19,
    height=2,
    state="disabled",
    command=next_question
)

next_button.grid(
    row=0,
    column=1,
    padx=10
)


# ======================================
# 7. RESULTS SCREEN
# ======================================

result_frame = tk.Frame(
    root,
    bg=BG
)


tk.Label(
    result_frame,
    text="QUIZ COMPLETED!",
    font=("Arial", 27, "bold"),
    fg=PURPLE,
    bg=BG
).pack(pady=(100, 25))


result_message = tk.Label(
    result_frame,
    text="",
    font=("Arial", 17, "bold"),
    fg=DARK,
    bg=BG
)

result_message.pack(pady=15)


result_score = tk.Label(
    result_frame,
    text="",
    font=("Arial", 38, "bold"),
    fg=PURPLE,
    bg=BG
)

result_score.pack(pady=15)


result_percentage = tk.Label(
    result_frame,
    text="",
    font=("Arial", 15),
    fg=GRAY,
    bg=BG
)

result_percentage.pack(pady=10)


# Restart button
tk.Button(
    result_frame,
    text="RESTART QUIZ",
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=restart_quiz
).pack(pady=30)


# Exit button
tk.Button(
    result_frame,
    text="EXIT APPLICATION",
    font=("Arial", 10),
    bg=BG,
    fg=GRAY,
    relief="flat",
    cursor="hand2",
    command=exit_application
).pack()


# ======================================
# 8. RUN APPLICATION
# ======================================

root.mainloop()

