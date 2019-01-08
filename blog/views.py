import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


class BlogView:

    """
    blog的列表，blog详情，和blog的提交，
    对blog的详情访问要做缓存，
    对blog对访问要有流量控制（throttle）
    发表blog必须要登录用户才能操作
    可以安blog的标签做筛选（标签是多标签的，array）
    可以对title做search
    """
    pass


class CommentView:
    """
    发表评论必须要先登录，拉取评论列表对时候必须要传入blog的id
    """
    pass


class LoginTokenView:

    """
    登录接口，用户模型使用django自带的User model，使用自带的login方法。要返回token。登录后
    才能操作的接口需要用token验证
    """


class RegisterView:

    """
    注册接口，注册后自动登录
    """



class LogoutView:

    """
    登出接口
    """

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")