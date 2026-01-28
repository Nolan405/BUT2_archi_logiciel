from .app import app, db
from .models import Questionnaire, Question

@app.cli.command()
def syncdb():
    db.drop_all()
    db.create_all()

    qz1 = Questionnaire.create_questionnaire('Culture Générale')
    qz1.add_question("Quelle est la capitale de la France ?")
    qz1.add_question("Qui a peint la Joconde ?")
    qz1.add_question("Quel est le plus grand mammifère marin ?")
    db.session.add(qz1)

    qz2 = Questionnaire.create_questionnaire('Géographie')
    qz2.add_question("Quel est le plus long fleuve du monde ?")
    qz2.add_question("Sur quel continent se trouve le mont Kilimandjaro ?")
    qz2.add_question("Quelle est la capitale du Japon ?")
    db.session.add(qz2)

    qz3 = Questionnaire.create_questionnaire('Histoire')
    qz3.add_question("En quelle année a commencé la Révolution française ?")
    qz3.add_question("Qui était le premier président des États-Unis ?")
    qz3.add_question("Quelle est la date de la chute du mur de Berlin ?")
    db.session.add(qz3)

    db.session.commit()
    print("Base de données synchronisée et initialisée avec succès !")