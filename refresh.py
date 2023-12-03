from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Simulated Database
latest_data = {'value': 'Initial Data'}

@app.route('/')
def index():
    return render_template('refresh.html', data=latest_data)

@app.route('/refresh', methods=['GET'])
def refresh_data():
    latest_data['value'] = 'New Data'
    return jsonify({'message': 'Data refreshed successfully', 'data': latest_data})

if __name__ == '__main__':
    app.run(debug=True)
