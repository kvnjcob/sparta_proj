from flask import Flask, request

import management

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index_page():
    return "Welcome to my server"


@app.route("/spartan/add", methods=["POST"])
def add_spartan():
    management.add_spartan_to_db()
    return f"the details are added to the database"


@app.route("/spartan/<spartan_id>", methods=["GET"])
def list_id(spartan_id):
    spartan_obj = management.retrieve_spartan(spartan_id)
    spartan_dict = vars(spartan_obj)
    return f"details for id {spartan_id}  : {spartan_dict}"


@app.route("/spartan/remove", methods=["POST"])
def remove_id():
    del_id = int(request.args.get("id"))
    outcome = management.remove_spartan(del_id)
    return f"{outcome}"


@app.route("/spartan", methods=["GET"])
def list_all_spartans():
    sparta_list = management.list_spartans()
    return f"{sparta_list}"


if __name__ == "__main__":
    app.run(debug=True)
