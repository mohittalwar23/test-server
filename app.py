from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
current_message = "No message yet"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET'])
def get_message():
    global current_message
    return jsonify({'message': current_message})

@app.route('/message', methods=['POST'])
def update_message():
    global current_message
    if request.is_json:
        content = request.get_json()
        current_message = content.get('message', 'No message provided')
        return jsonify({'status': 'Message updated'})
    else:
        return jsonify({'status': 'Failed', 'reason': 'Request is not JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)
