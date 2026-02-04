from flask_restx import Resource, Namespace, abort
from .models import Article, Comment, get_all_articles, create_article, get_article, get_all_comments, get_comment, create_comment
from .api_models import article_model, article_input_model, comment_model, comment_input_model

# creation du namespace, racine de tous les endpoints
ns = Namespace("api")

# definition d’une route
@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}



@ns.route("/articles")
class ArticleCollection(Resource):

    @ns.marshal_list_with(article_model)
    def get(self):
        return get_all_articles()
    
    @ns.expect(article_input_model)
    @ns.marshal_with(article_model)
    def post(self):
        create_article(title=ns.payload["title"], content=ns.payload["content"])
        return {},201



@ns.route("/articles/<int:id>")
@ns.response(404, 'Article not found')
class ArticleItem(Resource):
    @ns.marshal_with(article_model)
    def get(self,id):
        article = get_article(id)
        if article is None:
            abort(404,"Article not found")
        return article



@ns.route("/comments")
class CommentCollection(Resource):

    @ns.marshal_list_with(comment_model)
    def get(self):
        return get_all_comments()
    
    @ns.expect(comment_input_model)
    @ns.marshal_with(comment_model)
    def post(self):
        if get_article(ns.payload["article_id"]):
            create_comment(content=ns.payload["content"], article_id=ns.payload["article_id"])
            return {},201
        else:
            abort(400, "Not article found with this ID")



@ns.route("/comments/<int:id>")
@ns.response(404, 'comment not found')
class CommentItem(Resource):
    @ns.marshal_with(article_model)
    def get(self,id):
        comment = get_comment(id)
        if comment is None:
            abort(404,"Comment not found")
        return comment