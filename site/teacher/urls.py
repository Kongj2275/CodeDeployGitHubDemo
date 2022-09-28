from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-participantinfo', views.teacher_participantinfo_view,name='teacher-participantinfo'),
path('teacher-thanks', views.teacher_thanks_view,name='teacher-thanks'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-add-shortanswer', views.teacher_add_shortquestion_view,name='teacher-add-shortanswer'),
path('teacher-add-participantinformation', views.teacher_add_participantinfo_view,name='teacher-add-participantinformation'),
path('teacher-add-thanks', views.teacher_add_thanks_view,name='teacher-add-thanks'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('teacher-view-participantinfo', views.teacher_view_participantinfo_view,name='teacher-view-participantinfo'),
path('teacher-view-thanks', views.teacher_view_thanks_view,name='teacher-view-thanks'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('see-shortanswer/<int:pk>', views.see_shortanswer_view,name='see-shortanswer'),
path('see-participantinfo/<int:pk>', views.see_participantinfo_view,name='see-participantinfo'),
path('see-thanks/<int:pk>', views.see_thanks_view,name='see-thanks'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
path('remove-shortquestion/<int:pk>', views.remove_shortquestion_view,name='remove-shortquestion'),
path('remove-info/<int:pk>', views.remove_info_view,name='remove-info'),
path('remove-thanks/<int:pk>', views.remove_thanks_view,name='remove-thanks'),
]