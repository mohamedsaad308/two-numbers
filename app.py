from unittest import result
from flask import Flask, request, abort


def create_app(test_config=None):

    app = Flask(__name__)

    @app.route('/api/two-numbers', methods=['POST'])
    def hello_world():
        """
        This endpoint should take two numbers num1 and num2 between ±100*10^9
        and return 4 arithmetic operations between them
        Addition: num1 + num2
        Subtraction: num1 - num2
        Multiplication: nun1 x num2
        Division: num1 / num2
        """
        body = request.get_json()
        if body is None:
            abort(400)

        num1 = body.get("num1", None)
        num2 = body.get("num2", None)
        if num1 is None or num2 is None:
            abort(400)
        try:
            num1 = float(num1)
            num2 = float(num2)

        except ValueError:
            abort(400)
        if min(num1, num2) < -100 * 10**9 or max(num1, num2) > 100 * 10**9:
            abort(400)
        
        result = {}
        result["addition"] = num1 + num2
        result["substraction"] = num1 - num2 
        result["multiplication"] = num1*num2
        if num2 == 0:
            result["division"] = "Error, Zero division"
        else:
            result["division"] = num1/num2
        return {
                'success': True,
                'results' : result
            }
    @app.errorhandler(400)
    def bad_request(error):
        return {
            "success": False,
            "error": "400",
            "message": "Please provide two numbers between plus and minus one hundred billions"
        }, 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return {
            "success": False,
            "error": "405",
            "message" : "method not allowed"
        }, 405
    return app