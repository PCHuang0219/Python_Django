from ...sonic.models import *
from django.contrib.auth.models import User
import sys
        
class Database_Count():
    def __init__(self):
        pass
    
    def get_user(self):
        return User.objects.count()
    
    def get_article(self):
        return Article.objects.count()

    def get_message(self):
        return Message.objects.count()
    
    def get_message_user(self):
        return Message_User.objects.count()
    
    def get_article_tag(self):
        return Article_Tag.objects.count()
    
class Database_Table_Size():
    def __init__(self):
        pass
    
    def get_user(self):
        user = User()
        return sys.getsizeof(user) * User.objects.count()
    
    def get_article(self):
        article = Article()
        return sys.getsizeof(article) * Article.objects.count()

    def get_message(self):
        message = Message()
        return sys.getsizeof(message) * Message.objects.count()
    
    def get_message_user(self):
        message_user = Message_User()
        return sys.getsizeof(message_user) * Message_User.objects.count()
    
    def get_article_tag(self):
        article_tag = Article()
        return sys.getsizeof(article_tag) * Article_Tag.objects.count()