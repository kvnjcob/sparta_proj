from spartan import Spartan
import json

all_spartans = {}


def list_employees():
    global all_spartans

    load_from_json()
    for key in all_spartans:
        print(vars(all_spartans[key]))


def load_from_json():
    global all_spartans

    with open("data.json", "r") as data_file:
        temp_dict = json.load(data_file)

    for key in temp_dict:
        first_nm = temp_dict[key]["first_name"]
        last_nm = temp_dict[key]["last_name"]
        em_id = temp_dict[key]["emp_id"]

        emp1 = Spartan(first_nm, last_nm, em_id)

        all_spartans[em_id] = emp1
    return f"data loaded"
