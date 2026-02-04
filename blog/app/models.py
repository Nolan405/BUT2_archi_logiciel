from .extensions import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(500))
    comments = db.relationship("Comment", back_populates="article")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    article_id = db.Column(db.ForeignKey("article.id"))
    article = db.relationship("Article",back_populates="comments")



def get_all_articles():
    return Article.query.all()

def get_article(id):
    return Article.query.get(id)

def create_article(title,content):
    article = Article(title=title, content=content)
    db.session.add(article)
    db.session.commit()
    return article



def get_all_comments():
    return Comment.query.all()

def get_comment(id):
    return Comment.query.get(id)

def create_comment(content,article_id):
    content = Comment(content=content, article_id=article_id)
    db.session.add(content)
    db.session.commit()
    return content