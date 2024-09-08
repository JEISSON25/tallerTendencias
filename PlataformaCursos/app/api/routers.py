from rest_framework.routers import DefaultRouter
from ..user.views import *
from ..course.views import *
from ..lesson.views import *
from ..enrollment.views import *
from ..quiz.views import *
from ..question.views import *
from ..rol.views import *

router = DefaultRouter()

router.register(r'user', UserViewset, basename='user')
router.register(r'course', CourseViewset, basename='course')
router.register(r'lesson', LessonViewset, basename='lesson')
router.register(r'enrollment', EnrollmentViewset, basename='enrollment')
router.register(r'quiz', QuizViewset, basename='quiz')
router.register(r'question', QuestionViewset, basename='question')
router.register(r'rol', RolViewset, basename='rol')

urlpatterns = router.urls