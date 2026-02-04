from .app import db

class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    questions = db.relationship('Question', backref='questionnaire', lazy=True, cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id
    
    def get_nom(self):
        return self.name
    
    def set_nom(self, name):
        self.name = name

    def add_question_ouverte(self, enonce, reponse):
        numero = len(self.questions) + 1
        q = QuestionOuverte(numero=numero, enonce=enonce, reponse=reponse, questionnaire=self)
        db.session.add(q)
        return q

    def add_question_ferme(self, enonce, proposition1, proposition2, ind_reponse):
        numero = len(self.questions) + 1
        q = QuestionFerme(numero=numero, enonce=enonce, proposition1=proposition1, proposition2=proposition2, ind_reponse=ind_reponse, questionnaire=self)
        db.session.add(q)
        return q
    
    def supp_question(self, numero):
        for q in self.questions:
            if q.numero == numero:
                db.session.delete(q)
                return True
        return False
    
    @staticmethod
    def get_questionnaires():
        return Questionnaire.query.all()

    @staticmethod
    def get_questionnaire(id):
        return Questionnaire.query.get(id)

    @staticmethod
    def create_questionnaire(nom):
        q = Questionnaire(name=nom)
        db.session.add(q)
        return q
    
    @staticmethod
    def update_questionnaire(id, nom):
        q = Questionnaire.query.get(id)
        if q:
            q.set_nom(nom)
            db.session.commit()
            return q
        return None

    @staticmethod
    def delete_questionnaire(id):
        q = Questionnaire.query.get(id)
        if q:
            db.session.delete(q)
            db.session.commit()
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


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    enonce = db.Column(db.String(200))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'), nullable=False)
    type = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'polymorphic_on': type
    }

    def __init__(self, numero, enonce, questionnaire = None, questionnaire_id = None):
        self.numero = numero
        self.enonce = enonce
        if questionnaire:
            self.questionnaire = questionnaire
        else:
            self.questionnaire_id = questionnaire_id

    def get_numero(self):
        return self.numero
    
    def get_enonce(self):
        return self.enonce
    
    def question_to_json(self):
        return {
            "numero": self.numero,
            "enonce": self.enonce
        }


class QuestionOuverte(Question):
    __tablename__ = 'question_ouverte'
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse = db.Column(db.String(200))

    __mapper_args__ = {
        'polymorphic_identity': 'ouverte',
    }
    
    def __init__(self, numero, enonce, reponse, questionnaire = None, questionnaire_id = None):
        super().__init__(numero, enonce, questionnaire, questionnaire_id)
        self.reponse = reponse

    def get_reponse(self):
        return self.reponse
    
    def question_to_json(self):
        data = super().question_to_json()
        data['reponse'] = self.reponse
        return data
    

class QuestionFerme(Question):
    __tablename__ = 'question_ferme'
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    proposition1 = db.Column(db.String(200))
    proposition2 = db.Column(db.String(200))
    ind_reponse = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'fermee',
    }
    
    def __init__(self, numero, enonce, proposition1, proposition2, ind_reponse, questionnaire = None, questionnaire_id = None):
        super().__init__(numero, enonce, questionnaire, questionnaire_id)
        self.proposition1 = proposition1
        self.proposition2 = proposition2
        self.ind_reponse = ind_reponse

    def get_proposition1(self):
        return self.proposition1
    
    def get_proposition2(self):
        return self.proposition2
    
    def get_ind_reponse(self):
        return self.ind_reponse
    
    def question_to_json(self):
        data = super().question_to_json()
        data['propositions'] = [self.proposition1, self.proposition2]
        data['ind_reponse'] = self.ind_reponse
        return data
