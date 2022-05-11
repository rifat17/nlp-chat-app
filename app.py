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
    return render_template('chat.html')

@app.route("/whatsapp")
def whatsapp():
    return render_template('whatsapp.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    response = answer = ChatwithUser.reply(message)
    return jsonify({'status':'OK','answer':response})


if __name__ == "__main__":
    app.run(debug=True)