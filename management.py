from spartan import Spartan
import json

all_spartans = {}


def list_spartans():
    global all_spartans
    temp_dict = {}

    load_from_json()
    for key in all_spartans:
        temp_dict[key] = vars(all_spartans[key])
    return temp_dict


def retrieve_spartan(spartan_id):
    global all_spartans
    load_from_json()
    int_id = int(spartan_id)

    if int_id in all_spartans.keys():
        return all_spartans[int_id]
    else:
        return f"spartan id {spartan_id} not in database "


def load_from_json():
    global all_spartans

    with open("data.json", "r") as data_file:
        temp_dict = json.load(data_file)

    for key in temp_dict:
        first_nm = temp_dict[key]["first_name"]
        last_nm = temp_dict[key]["last_name"]
        emp_id = temp_dict[key]["emp_id"]

        temp_spartan = Spartan(first_nm, last_nm, emp_id)

        all_spartans[emp_id] = temp_spartan
    return f"data loaded"


def save_to_json():
    global all_spartans
    temp_spartan_dict = {}

    for spartan_id in all_spartans:
        employee_obj = all_spartans[spartan_id]
        spartan_dict = vars(employee_obj)
        temp_spartan_dict[spartan_id] = spartan_dict

    with open("data.json", "w") as data_file:
        json.dump(temp_spartan_dict, data_file)
        print("Object formatted as dictionary and saved to JSON")


def remove_spartan(sparta_id):
    global all_spartans

    load_from_json()

    if sparta_id in all_spartans.keys():
        del all_spartans[sparta_id]
        save_to_json()
        return f"id : {sparta_id} deleted"
    else:
        return f"Id does not exist in file"


