from flask import jsonify, abort, make_response, request, url_for
from .app import app
from .models import Questionnaire



@app.route('/quiz/api/v1.0/questionnaires', methods=['GET'])
def get_questionnaires():
    public_questionnaires = []
    all_questionnaires = Questionnaire.get_questionnaires()
    
    for questionnaire in all_questionnaires:
        public_questionnaires.append(questionnaire.questionnaire_to_json())
        
    return jsonify({'questionnaires': public_questionnaires})



@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['GET'])
def get_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.get_questionnaire(questionnaire_id)
    if questionnaire is None:
        return abort(404)
    
    questionnaire.questionnaire_to_json()
    return jsonify({'questionnaires': questionnaire.questionnaire_to_json()})



@app.route('/quiz/api/v1.0/questionnaires', methods=['POST'])
def create_questionnaire():
    if not request.json or not 'nom' in request.json:
        return abort(400)
    
    nom_questionnaire = request.json['nom']
    nouvelle_quest = Questionnaire.create_questionnaire(nom_questionnaire)
    return jsonify({'result': nouvelle_quest.questionnaire_to_json()}), 201



@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['PUT'])
def update_questionnaire(questionnaire_id):
    if not request.json or not 'nom' in request.json:
        return abort(400)
    
    new_nom = request.json['nom']
    update_quest = Questionnaire.update_questionnaire(questionnaire_id, new_nom)
    if update_quest is None:
        return abort(404)
    return jsonify({'result': update_quest.questionnaire_to_json()}), 201



@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['DELETE'])
def delete_questionnaire(questionnaire_id):
    if not 'numero' in request.json:
        boolean = Questionnaire.delete_questionnaire(questionnaire_id)
        if not boolean:
            return abort(404)
        return jsonify({"status": "deleted"})



@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['POST'])
def create_question(questionnaire_id):
    if not request.json or not 'enonce' in request.json:
        return abort(400)
    
    questionnaire = Questionnaire.get_questionnaire(questionnaire_id)
    enonce = request.json['enonce']
    question = questionnaire.add_question(enonce)
    return jsonify({'result': question.question_to_json()}), 201



@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:question_num>', methods=['DELETE'])
def delete_question(questionnaire_id, question_num):
    
    questionnaire = Questionnaire.get_questionnaire(questionnaire_id)
    boolean = questionnaire.supp_question(question_num)
    if not boolean:
        return abort(404)
    return jsonify({"status": "deleted"})



@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['GET'])
def get_questions(questionnaire_id):
    questionnaire = Questionnaire.get_questionnaire(questionnaire_id)
    questions = questionnaire.get_questions()
    if questions is None:
        return abort(404)
    return jsonify({'result': questions.question_to_json()}), 201