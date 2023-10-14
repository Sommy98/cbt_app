import time
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/test',methods=['GET'])
def test():
    print("hello sommy on the beat")
        


test()

if __name__ == "__main__":
    app.run()

# def run_timed_quiz(questions, time_limit):
    # score = 0
    # current_question = 0
    # start_time = 0
    
    # @app.route('/test',methods=['GET'])
    # def test():
    #     print('Here is the testing page')

    # @app.route('/', methods=['GET', 'POST'])
    # def quiz():
    #     nonlocal score, current_question, start_time
    #     if request.method == 'POST':
    #         user_answer = int(request.form['answer'])

    #         if time.time() - start_time > time_limit:
    #             flash(f"Time's up! The correct answer is {questions[current_question]['answer']}.")
    #         else:
    #             if user_answer == questions[current_question]['answer']:
    #                 score += 1

    #         current_question += 1

    #         if current_question < len(questions):
    #             return render_template('quiz.html', question=questions[current_question], score=score, time_remaining=time_limit)
    #         else:
    #             flash(f"Quiz completed! Your score: {score}/{len(questions)}")
    #             return render_template('quiz.html', score=score)

    #     if request.method == 'GET':
    #         score = 0
    #         current_question = 0
    #         start_time = time.time()

    #     return render_template('quiz.html', question=questions[current_question], score=score, time_remaining=time_limit)

    # if __name__ == "__main__":
    #     app.run()

# Define the questions
# quiz_questions = [
#     {
#         'question': 'What is the capital of France?',
#         'options': ['A. London', 'B. Paris', 'C. Rome', 'D. Madrid'],
#         'answer': 2
#     },
#     {
#         'question': 'Which planet is known as the Red Planet?',
#         'options': ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
#         'answer': 2
#     },
#     {
#         'question': 'Who painted the Mona Lisa?',
#         'options': ['A. Vincent van Gogh', 'B. Pablo Picasso', 'C. Leonardo da Vinci', 'D. Michelangelo'],
#         'answer': 3
#     }
# ]

# time_limit = 10  # Time limit for each question in seconds

# Run the timed quiz as a web page
# run_timed_quiz(quiz_questions, time_limit)
