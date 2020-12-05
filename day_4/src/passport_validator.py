from passport_schema import PassportSchema

class PassportValidator:

    def __init__(self, passport):
        self.passport = passport
        self.schema = PassportSchema()
    
    def validate_passport(self):
        return self.schema.load(self.passport)
        