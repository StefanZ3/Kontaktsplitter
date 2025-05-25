class LetterSalutationGenerator:
    def get_letter_salutation(self, parsed_contact):
        """Generiert die Briefanrede mithilfe Geschlecht, Titel und Namen."""
        first_name = parsed_contact["first_name"]
        last_name = parsed_contact["last_name"]
        
        titles = parsed_contact["titles"]
        #titles = [t.strip() for t in parsed_contact["titles"].split(",") if t.strip()]
        gender = parsed_contact["gender"]

        if gender == "männlich":
            first_part = "Sehr geehrter Herr"
        elif gender == "weiblich":
            first_part = "Sehr geehrte Frau"
        else:
            return "Sehr geehrte Damen und Herren"

        # Die Titel Doktor und Professor werden auf ihre Kurzform gebracht, die anderen werden übernommen
        titles_for_letter_salutation = []
        if titles:
            for title in titles:
                if "dr." in title.lower():
                    title = "Dr."
                elif "prof" in title.lower():
                    title = "Prof."
                titles_for_letter_salutation.append(title)
        title_part = " ".join(titles_for_letter_salutation)

        last_name_part = last_name

        letter_salutation = " ".join(part for part in [first_part, title_part, last_name_part] if part)
        return letter_salutation
