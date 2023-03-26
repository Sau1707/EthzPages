LINE = ["Tue, 25 Sep 2007 14:10:00 GMT", "Thu, 03 Feb 2022 08:05:36 GMT", "17 Oct 2012 11:46:57 GMT"]

HEADERS = { 
    "If-Modified-Since": LINE[0]
}

DEPARTMENTS = { # https://ethz.ch/en/the-eth-zurich/organisation/departments-and-competence-centres/departments.html
    # Architecture and Civil Engineering
    "D-ARCH": "Architecture",
    "D-BAUG": "Civil, Environmental and Geomatic Engineering",
    # Engineering Sciences
    "D-BSSE": "Biosystems Science and Engineering",
    "D-INFK": "Computer Science",
    "D-ITET": "Information Technology and Electrical Engineering",
    "D-MAVT": "Mechanical and Process Engineering",
    "D-MATL": "Materials",
    # Natural Sciences and Mathematics
    "D-BIOL": "Biology",
    "D-CHAB": "Chemistry and Applied Biosciences",
    "D-MATH": "Mathematics",
    "D-PHYS" : "Physics",  
    # System-​oriented Natural Sciences 
    "D-ERDW": "Earth Sciences",
    "D-USYS": "Environmental Systems Science",
    "D-HEST": "Health Sciences and Technology",
    # Management and Social Sciences
    "D-MTEC": "Management, Technology and Economics",
    "D-GESS": "Humanities, Social and Political Sciences"
}

GENDERS = {
    "Studentin": "female",
    "Student": "male",
    #"Mitarbeiterin": "female",
    #"Mitarbeiter": "male",
    #"Hörerin": "female",
    #"Hörer": "male",
    #"Dozent": None,
    #"Professur": None,
    #"Pensioniert": None,
    #"PSI": None,
    #"Paul Scherrer Institut": None,
    #"Gast": None,
    #"Institute of Molecular Biology & Biophysics": None,
    #"Militärakademie": None
}