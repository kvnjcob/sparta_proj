from spartan import Spartan
import json
from flask import request

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
        birth_yr = temp_dict[key]["birth_year"]
        birth_mn = temp_dict[key]["birth_month"]
        birth_dy = temp_dict[key]["birth_day"]
        course = temp_dict[key]["course"]
        stream = temp_dict[key]["stream"]

        temp_spartan = Spartan(first_nm, last_nm, emp_id, birth_yr, birth_mn, birth_dy, course, stream)

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


def add_spartan_to_db():
    global all_spartans

    load_from_json()

    spartan_details = request.get_json()

    spartan_f_n = spartan_details["first_name"]
    spartan_l_n = spartan_details["last_name"]
    spartan_e_id = spartan_details["emp_id"]
    spartan_byr = spartan_details["birth_year"]
    spartan_bmn = spartan_details["birth_month"]
    spartan_bdy = spartan_details["birth_day"]
    spartan_crse = spartan_details["course"]
    spartan_strm = spartan_details["stream"]

    spartan_temp = Spartan(spartan_f_n, spartan_l_n, spartan_e_id, spartan_byr, spartan_bmn, spartan_bdy, spartan_crse,
                           spartan_strm)

    all_spartans[spartan_temp.get_emp_id()] = spartan_temp

    save_to_json()
