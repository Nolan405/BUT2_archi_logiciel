from .app import db

class Questionnaire(db.Model):

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

    def get_questions(self):
        self.questions

    def add_question(self, enonce):
        numero = len(self.questions) + 1
        q = Question(numero=numero, enonce=enonce, questionnaire_id=self.id)
        self.questions.append(q)
        return q
    
    def supp_question(self, numero):
        for q in self.questions:
            if q.get_numero() == numero:
                self.questions.remove(q)
                return True
        return False
    
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
    
    for enonce in liste_enonces:
        questionnaire.add_question(enonce)


# from .app import db

# class Questionnaire(db.Model):
#     __tablename__ = 'questionnaire'
#     # Définition des colonnes pour SQLAlchemy
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     # Relation : un questionnaire possède plusieurs questions
#     # backref crée une propriété 'questionnaire' dans l'objet Question
#     questions = db.relationship('Question', backref='questionnaire', lazy=True, cascade="all, delete-orphan")

#     def __init__(self, name):
#         self.name = name

#     def get_id(self):
#         return self.id
    
#     def get_nom(self):
#         return self.name
    
#     def set_nom(self, name):
#         self.name = name

#     def add_question(self, enonce):
#         # On calcule le numéro basé sur le nombre de questions existantes
#         numero = len(self.questions) + 1
#         q = Question(numero=numero, enonce=enonce, questionnaire_id=self.id)
#         self.questions.append(q)
#         return q
    
#     def supp_question(self, numero):
#         for q in self.questions:
#             if q.numero == numero:
#                 db.session.delete(q)
#                 return True
#         return False
    
#     @staticmethod
#     def get_questionnaires():
#         # Remplace la liste locale par une requête SQL
#         return Questionnaire.query.all()

#     @staticmethod
#     def get_questionnaire(id):
#         # Cherche par clé primaire en base de données
#         return Questionnaire.query.get(id)

#     @staticmethod
#     def create_questionnaire(nom):
#         q = Questionnaire(name=nom)
#         db.session.add(q)
#         # On ne fait pas commit ici pour laisser la main à l'appelant (commands.py)
#         return q
    
#     @staticmethod
#     def update_questionnaire(id, nom):
#         q = Questionnaire.query.get(id)
#         if q:
#             q.set_nom(nom)
#             db.session.commit()
#             return q
#         return None

#     @staticmethod
#     def delete_questionnaire(id):
#         q = Questionnaire.query.get(id)
#         if q:
#             db.session.delete(q)
#             db.session.commit()
#             return True
#         return False

#     def questionnaire_to_json(self):
#         return {
#             "id": self.id,
#             "nom": self.name,
#             "questions": [q.question_to_json() for q in self.questions]
#         }


# class Question(db.Model):
#     __tablename__ = 'question'
#     id = db.Column(db.Integer, primary_key=True)
#     numero = db.Column(db.Integer)
#     enonce = db.Column(db.String(200))
#     # Clé étrangère pour lier à la table Questionnaire
#     questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'), nullable=False)

#     def __init__(self, numero, enonce, questionnaire_id=None):
#         self.numero = numero
#         self.enonce = enonce
#         self.questionnaire_id = questionnaire_id

#     def get_numero(self):
#         return self.numero
    
#     def get_enonce(self):
#         return self.enonce
    
#     def question_to_json(self):
#         return {
#             "numero": self.numero,
#             "enonce": self.enonce
#         }