class ContactParser:
    def parse(self, input_contact):
        gender = self.get_gender(input_contact)

    def get_gender(self, input_contact: str):
        if 'Herr' in input_contact:
            return 'männlich'
        elif 'Frau' in input_contact:
            return 'weiblich'
        return None
    


