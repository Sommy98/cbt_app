import time
import random
from flask import Flask, render_template, request, flash, redirect, url_for

fiftyapp = Flask(__name__)
fiftyapp.secret_key = 'secret_key'

# Define the questions
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'option_a': 'A. London',
        'option_b': 'B. Paris',
        'option_c': 'C. Rome',
        'option_d': 'D. Madrid',
        'answer': 'option_b',
        'difficulty': 'Easy',
        'points': 1,
        'eliminated_options': ['option_c', 'option_d']
    },
    {
        'question': 'What is the capital of Lagos?',
        'option_a': 'A. Ikeja',
        'option_b': 'B. Paris',
        'option_c': 'C. Abuja',
        'option_d': 'D. London',
        'answer': 'option_a',
        'difficulty': 'Medium',
        'points': 2,
        'eliminated_options': ['option_b', 'option_d']
    },
    {
        'question': 'What is the capital of Nigeria?',
        'option_a': 'A. Ikeja',
        'option_b': 'B. Paris',
        'option_c': 'C. Abuja',
        'option_d': 'D. London',
        'answer': 'option_c',
        'difficulty': 'Hard',
        'points': 3,
        'eliminated_options': ['option_b', 'option_d']
    },
]

# quiz_questions = random.shuffle(quiz_questions)

random.shuffle(quiz_questions)  # Randomize the order of questions

question_index = 0  # Set the current question index
score = 0  # Set the score
start_time = 0  # Store the start time for each question
time_limit = 300  # Set the time limit for each question in seconds

# Route for displaying and handling the questions
@fiftyapp.route('/fifty', methods=['GET', 'POST'])
def test():
    
    print("hello here")
    global question_index, score, start_time

    if request.method == 'POST':
        user_answer = request.form.get('option')
        current_question = quiz_questions[question_index]

        if user_answer == current_question['answer']:
            score += current_question['points']
            flash("You got the question right! Well done!")
        else:
            flash("Sorry, that's incorrect.")

        question_index += 1

        if question_index >= len(quiz_questions):
            flash(f"Thanks for taking our quiz. Your score is {score} / {sum(question['points'] for question in quiz_questions)}")
            question_index = 0  # Reset the question index
            score = 0  # Reset the score
            return redirect(url_for('result'))

    if question_index < len(quiz_questions):
        if request.method == 'GET':
            start_time = time.time()

        current_question = quiz_questions[question_index]
        remaining_time = start_time + time_limit - time.time()
        return render_template('fifty.html', question=current_question, current_question=question_index, score=score, remaining_time=remaining_time)
    else:
        return redirect(url_for('result'))
    

@fiftyapp.route('/result', methods=['GET'])
def result():
    global question_index, score
    question_index = 0  # Reset the question index
    score = 0  # Reset the score
    return render_template('result.html')

# Route for handling the "50-50" feature
@fiftyapp.route('/fifty_fifty', methods=['POST'])
def fifty_fifty():
    global question_index

    current_question = quiz_questions[question_index]
    eliminated_options = current_question.get('eliminated_options', [])
    options = ['option_a', 'option_b', 'option_c', 'option_d']
    options_to_eliminate = random.sample(eliminated_options, 2)
    for option in options:
        if option in options_to_eliminate:
            current_question[option] = ''  # Empty the eliminated options

    return redirect(url_for('test'))


if __name__ == "__main__":
    fiftyapp.run(debug=True, port=6000)
