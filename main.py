from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index_page():
    return "Welcome to my server"


@app.route("/spartan/add", methods=["POST"])
def add_spartan():
    spartan_data = request.json
    f_n = spartan_data["first_name"]
    l_n = spartan_data["last_name"]
    e_id = spartan_data["emp_id"]

    return f"{f_n} {l_n} has ID : {e_id}"


@app.route("/spartan/<spartan_id>", methods=["GET"])
def list_id(spartan_id):
    return f"ids : {spartan_id}"


@app.route("/spartan/remove", methods=["POST"])
def remove_id():
    del_id = request.args.get("id")
    return f"{type(del_id)}"


@app.route("/spartan", methods=["GET"])
def list_all_spartans():
    sparta_list = management.list_employees()
    return sparta_list


if __name__ == "__main__":
    app.run(debug=True)
