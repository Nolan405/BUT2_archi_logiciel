class Questionnaire:

    cpt_id = 1
    questionnaires = []

    def __init__(self, name):
        self.name = name
        self.id = Questionnaire.cpt_id
        Questionnaire.cpt_id += 1
        Questionnaire.questionnaires.append(self)

    def get_id(self):
        return self.id
    
    def get_nom(self):
        return self.name
    
    @staticmethod
    def get_questionnaires():
        return Questionnaire.questionnaires

    @staticmethod
    def get_questionnaire(id):
        for q in Questionnaire.questionnaires:
            if q.get_id() == id:
                return q

    @staticmethod
    def create_questionnaire(nom):
        Questionnaire(nom)

    @staticmethod
    def delete_questionnaire(id):
        for q in Questionnaire.questionnaires:
            if q.get_id() == id:
                Questionnaire.questionnaires.remove(q)

    def questionnaire_to_json(self):
        json = {
            "id": self.get_id(),
            "nom": self.get_nom()
        }
        return json


themes = [
    "Culture Générale", "Géographie", "Histoire", "Sciences", 
    "Cinéma", "Sport", "Musique", "Littérature", 
    "Technologie", "Gastronomie"
]

for theme in themes:
    Questionnaire.create_questionnaire(theme)

