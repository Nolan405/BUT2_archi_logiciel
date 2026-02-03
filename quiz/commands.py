from .app import app, db
from .models import Questionnaire, QuestionOuverte, QuestionFerme

@app.cli.command()
def syncdb():
    db.drop_all()
    db.create_all()

    qz1 = Questionnaire.create_questionnaire('Culture Générale')
    qz1.add_question_ouverte("Quelle est la capitale de la France ?", "Paris")
    qz1.add_question_ferme("Qui a peint la Joconde ?", "Léonard de Vinci", "Picasso", 1)
    qz1.add_question_ferme("Quel est le plus grand mammifère marin ?", "La baleine bleue", "L'éléphant", 1) 

    qz2 = Questionnaire.create_questionnaire('Géographie')
    qz2.add_question_ferme("Quel est le plus long fleuve du monde ?", "Le Nil", "L'Amazone", 2)
    qz2.add_question_ouverte("Sur quel continent se trouve le mont Kilimandjaro ?", "Afrique")
    qz2.add_question_ouverte("Quelle est la capitale du Japon ?", "Tokyo")


    qz3 = Questionnaire.create_questionnaire('Histoire')
    qz3.add_question_ferme("En quelle année a commencé la Révolution française ?", "1789", "1815", 1)
    qz3.add_question_ouverte("Qui était le premier président des États-Unis ?", "George Washington")
    qz3.add_question_ouverte("Quelle est la date de la chute du mur de Berlin ?", "1989")

    db.session.commit()
    print("Base de données synchronisée et initialisée avec succès !")