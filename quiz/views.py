from flask import jsonify, abort, make_response, request, url_for
from .app import app
from .models import Questionnaire



@app.route('/quiz/api/v1.0/questionnaires', methods=['GET'])
def get_questionnaires():
    public_questionnaires = []
    for questionnaire in Questionnaire.get_questionnaires():
        public_questionnaires.append(questionnaire)
        
    return jsonify({'questionnaires': public_questionnaires})