class Spartan:

    def __init__(self, f_name, l_name, e_id):
        self.first_name = f_name
        self.last_name = l_name
        # self.birth_year = birth_year
        # self.birth_month = birth_month
        # self.birth_day = birth_day
        # self.course = course
        # self.stream = stream
        self.emp_id = e_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_year(self):
        return self.birth_year

    def get_birth_month(self):
        return self.birth_month

    def get_birth_day(self):
        return self.birth_day

    def get_course(self):
        return self.course

    def get_stream(self):
        return self.stream

    def get_emp_id(self):
        return self.emp_id

    def set_first_name(self, new_f_name):
        self.first_name = new_f_name

    def set_last_name(self, new_l_name):
        self.last_name = new_l_name

    def set_birth_year(self, new_birth_year):
        self.birth_year = new_birth_year

    def set_birth_month(self, new_birth_month):
        self.birth_month = new_birth_month

    def set_birth_day(self, new_birth_day):
        self.birth_day = new_birth_day

    def set_course(self, new_course):
        self.course = new_course

    def set_stream(self, new_stream):
        self.stream = new_stream

    def set_emp_id(self, new_emp_id):
        self.emp_id = new_emp_id


if __name__ == "__main__":
    new_spartan = Spartan("Kevin", "Jacob", 1)
    spartan_dict = vars(new_spartan)

    print(spartan_dict)