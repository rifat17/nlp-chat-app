from flask import Flask, render_template, request, jsonify

import ChatwithUser

# while True:
#     user_input = input()
    
#     if user_input == "quit":
#         print("Program exited successfully.")
#         break
#     print("Your input is :", user_input)
#     answer = ChatwithUser.reply(user_input)
#     print("Answer: ", answer)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('whatsapp.html')

@app.route("/chat")
def whatsapp():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    answer, closest_question = ChatwithUser.reply(message)
    return jsonify({'status':'OK','answer':answer, 'closest_question': str(closest_question[0])}, )


if __name__ == "__main__":
    app.run(debug=True)