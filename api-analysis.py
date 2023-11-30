from flask import Flask, request, jsonify
from app import performm_analyses

app = Flask(__name__)

# #Developing an api end point that will trigger the analysis script
@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    # Get the data from the request
    data = request.get_data(as_text=True)
    # Perform analyses
    results = perform_analyses(data)
    # Return the analysis results as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
