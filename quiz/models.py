class Questionnaire:

    cpt_id = 1
    questionnaires = []

    def __init__(self, name):
        self.name = name
        self.id = Questionnaire.cpt_id
        self.questions = []
        Questionnaire.cpt_id += 1
        Questionnaire.questionnaires.append(self)

    def get_id(self):
        return self.id
    
    def get_nom(self):
        return self.name
    
    def set_nom(self, name):
        self.name = name

    def add_question(self, question):
        self.questions.append(question)
    
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
        return Questionnaire(nom)
    
    @staticmethod
    def update_questionnaire(id, nom):
        for q in Questionnaire.questionnaires:
            if q.get_id() == id:
                q.set_nom(nom)
                return q
        return None

    @staticmethod
    def delete_questionnaire(id):
        for q in Questionnaire.questionnaires:
            if q.get_id() == id:
                Questionnaire.questionnaires.remove(q)
                return True
        return False

    def questionnaire_to_json(self):
        questions_json = []
        for question in self.questions:
            questions_json.append(question.question_to_json())

        json = {
            "id": self.get_id(),
            "nom": self.get_nom(),
            "questions": questions_json
        }
        return json


class Question:

    def __init__(self, numero, enonce):
        self.numero = numero
        self.enonce = enonce

    def get_numero(self):
        return self.numero
    
    def get_enonce(self):
        return self.enonce
    
    def question_to_json(self):
        json = {
            "numero": self.get_numero(),
            "enonce": self.get_enonce()
        }
        return json
    



questions_data = {
    "Culture Générale": [
        "Quelle est la capitale de la France ?",
        "Qui a peint la Joconde ?",
        "Quel est le plus grand mammifère marin ?"
    ],
    "Géographie": [
        "Quel est le plus long fleuve du monde ?",
        "Sur quel continent se trouve le mont Kilimandjaro ?",
        "Quelle est la capitale du Japon ?"
    ],
    "Histoire": [
        "En quelle année a commencé la Révolution française ?",
        "Qui était le premier président des États-Unis ?",
        "Quelle est la date de la chute du mur de Berlin ?"
    ]
}

for theme, liste_enonces in questions_data.items():
    questionnaire = Questionnaire.create_questionnaire(theme)
    
    for i, enonce in enumerate(liste_enonces, 1):
        nouvelle_question = Question(i, enonce)
        questionnaire.add_question(nouvelle_question)
