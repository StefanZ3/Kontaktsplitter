TITEL_METADATA = {
    # Akademische Titel
    "Professor": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": True},
    "Professorin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": True},
    "Prof.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": False},  # In der Anrede nicht abgekürzt!
    "Dr.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr.-Ing.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. h.c. mult.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. rer. nat.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. med.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. jur.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. phil.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. rer. pol.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. theol.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. paed.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. habil.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. rer. oec.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. rer. soc.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dr. h. c.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": True},
    "Dipl.-Ing.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": False},
    "Dipl.-Kfm.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": False},
    "Dipl.-Volksw.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": False},
    "M.Sc.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": False},
    "B.Sc.": {"geschlecht": "unisex", "nationalitaet": "DE", "include_in_salutation": False},

    # Adels-/Monarchentitel
    "Kaiser": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Kaiserin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "König": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Königin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Erzherzog": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Erzherzogin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Großherzog": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Großherzogin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Kurfürst": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Kurfürstin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Fürst": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Fürstin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Herzog": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Herzogin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Markgraf": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Markgräfin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Landgraf": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Landgräfin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Pfalzgraf": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Pfalzgräfin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Graf": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": True},
    "Gräfin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": True},
    "Freiherr": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": True},
    "Freifrau": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": True},
    "Freifräulein": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": True},
    "Baron": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": True},
    "Baronin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": True},
    "Edler": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": True},
    "Edle": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": True},
    "Prinz": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Prinzessin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False},
    "Thronfolger": {"geschlecht": "männlich", "nationalitaet": "DE", "include_in_salutation": False},
    "Thronfolgerin": {"geschlecht": "weiblich", "nationalitaet": "DE", "include_in_salutation": False}
}

NORMALIZED_TITLES = {
    "prof.": "Professor",
    "professor": "Professor",
    "professorin": "Professorin"
}

SALUTATIONS = {
    "Herr": {"geschlecht": "männlich", "nationalitaet": "DE"},
    "Frau": {"geschlecht": "weiblich", "nationalitaet": "DE"},
    "Ms.": {"geschlecht": "weiblich", "nationalitaet": "EN"},
    "Miss": {"geschlecht": "weiblich", "nationalitaet": "EN"},
    "Mrs.": {"geschlecht": "weiblich", "nationalitaet": "EN"},
    "Mr.": {"geschlecht": "männlich", "nationalitaet": "EN"},
    "Mme.": {"geschlecht": "weiblich", "nationalitaet": "FR"},
    "M.": {"geschlecht": "männlich", "nationalitaet": "FR"},
    "Madame": {"geschlecht": "weiblich", "nationalitaet": "FR"},
    "Monsieur": {"geschlecht": "männlich", "nationalitaet": "FR"},
    "Señora": {"geschlecht": "weiblich", "nationalitaet": "ES"},
    "Señorita": {"geschlecht": "weiblich", "nationalitaet": "ES"},
    "Señor": {"geschlecht": "männlich", "nationalitaet": "ES"}
}

LASTNAME_PREFIXES = {"von", "van", "de", "del", "di", "le", "la", "du"}

SALUTATIONS_BY_LANGUAGE = {
    "DE": {
        "männlich": "Sehr geehrter Herr",
        "weiblich": "Sehr geehrte Frau",
        "divers": "Sehr geehrte Damen und Herren",
        "default": "Sehr geehrte Damen und Herren"
    },
    "EN": {
        "männlich": "Dear Mr.",
        "weiblich": "Dear Ms.",
        "divers": "Dear Sir or Madam",
        "default": "Dear Sir or Madam"
    },
    "FR": {
        "männlich": "Monsieur",
        "weiblich": "Madame",
        "divers": "Mesdames, Messieurs",
        "default": "Mesdames, Messieurs"
    },
    "ES": {
        "männlich": "Estimado Señor",
        "weiblich": "Estimada Señora",
        "divers": "Estimados señores",
        "default": "Estimados señores"
    }
}
