from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input"
    return render_template("index.html", result=result)
@app.route("/calculate/<int:num1>/<operation>/<int:num2>", methods = ["GET", "POST"])
def calculate(num1, operation, num2):
    if request.method == "GET":
        result = None
        
        try:
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input"
    return f"{result}"
@app.route("/calculate", methods = ["GET", "POST"])
# def calculate():
#     if request.method == "GET":
#         result = None
#         num1 =request.args.get("num1")
#         num2 = request.args.get("num2")
#         operation = request.args.get("operation")
#         try:
#             if operation == "+":
#                 result = num1 + num2
#             elif operation == "-":
#                 result = num1 - num2
#             elif operation == "*":
#                 result = num1 * num2
#             elif operation == "divide":
#                 result = num1 / num2 if num2 != 0 else "Error: Division by zero"
#             else:
#                 result = "Invalid operation"
#         except ValueError:
#             result = "Invalid input"
#     return f"{result}"
    
    

@app.route("/about/<name>", methods = ["Get", "Post"])
def iloveyou(name):
    
    return render_template("ilob.html", name = name)
    
if __name__ == "__main__":
    app.run(debug=True)
