from flask import Flask, request, jsonify
from modules import FizzBuzzCompute
from flask_swagger_ui import get_swaggerui_blueprint

# Create a Flask web application
app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/static/api-doc/swagger-api.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "FizzBuzz Server"
    },
)

app.register_blueprint(swaggerui_blueprint)



# keep count of hits
counter = {}


# add middleware to count requests
@app.before_request
def count_requests():
    str1 = request.args.get("str1")
    str2 = request.args.get("str2")

    if str1 is not None and str2 is not None:
        if counter.get((str1, str2)):
            counter[(str1, str2)] += 1
        else:
            counter[(str1, str2)] = 1


# Define a route for the root URL
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/api/get-result', methods=['GET'])
def GetFizzBuzzResult():
    n1 = request.args.get("n1")
    n2 = request.args.get("n2")
    limit = request.args.get("limit")
    str1 = request.args.get("str1")
    str2 = request.args.get("str2")

    if n1 is None or n2 is None or limit is None or str1 is None or str2 is None:
        return jsonify({"Error": "Invalid parameters"}), 400

    try:
        result = FizzBuzzCompute.GetFizzBuzzResult(int(n1), int(n2), int(limit), str1, str2)
        return result, 200

    except:
        return "Internal Server Error", 500


# returns the count of the most queried term
@app.route('/api/get-statistics', methods=['GET'])
def GetStatistics():
    if not counter:
        return "No Hits received yet!", 200

    max_key = max(counter, key=lambda k: counter[k])
    max_value = counter[max_key]

    result = {
        'key': max_key,
        'hits': max_value
    }

    return jsonify(result), 200


@app.route('/api/get-statistics-by-keys', methods=['GET'])
def GetStatisticsByKeys():
    str1 = request.args.get("p1")
    str2 = request.args.get("p2")

    if str1 is None or str2 is None:
        return "Invalid Parameters", 400

    try:
        if counter.get((str1, str2)):
            result = {
                'keys': (str1, str2),
                'hits': counter[(str1, str2)]
            }
        else:
            result = {
                'keys': (str1, str2),
                'hits': 0
            }
        return jsonify(result), 200

    except:
        return "Internal Server Error", 500


# Run the web server
if __name__ == '__main__':
    app.run(debug=True)
