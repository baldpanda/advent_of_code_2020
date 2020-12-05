class PassportReader:
    def read_in_data(self, path_to_data):
        with open(path_to_data, "r") as f:
            passports = f.read()
        passports = passports.split("\n\n")
        passports = [passport_string.replace("\n", " ") for passport_string in passports]
        passports_dicts  = []
        for i in passports:
            passports_dicts.append(dict(item.split(":") for item in i.split(" ")))
        return passports_dicts