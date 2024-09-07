from rest_framework.routers import DefaultRouter
from ..user.views import *
from ..course.views import *
from ..lesson.views import *
from ..enrollment.views import *
from ..quiz.views import *
from ..question.views import *

router = DefaultRouter()

router.register(r'user', UserViewset, basename='user')
router.register(r'course', UserViewset, basename='course')
router.register(r'lesson', UserViewset, basename='lesson')
router.register(r'enrollment', UserViewset, basename='enrollment')
router.register(r'quiz', UserViewset, basename='quiz')
router.register(r'question', UserViewset, basename='question')

urlpatterns = router.urls