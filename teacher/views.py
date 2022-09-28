from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from quiz import models as QMODEL
from student import models as SMODEL
from quiz import forms as QFORM


#for showing signup/login button for teacher
def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'teacher/teacherclick.html')

def teacher_signup_view(request):
    userForm=forms.TeacherUserForm()
    teacherForm=forms.TeacherForm()
    mydict={'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=forms.TeacherUserForm(request.POST)
        teacherForm=forms.TeacherForm(request.POST,request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacher=teacherForm.save(commit=False)
            teacher.user=user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('teacherlogin')
    return render(request,'teacher/teachersignup.html',context=mydict)



def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_student':SMODEL.Student.objects.all().count()
    }
    return render(request,'teacher/teacher_dashboard.html',context=dict)

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_exam_view(request):
    return render(request,'teacher/teacher_exam.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_participantinformation_view(request):
    return render(request,'teacher/teacher_add_participantinformation.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_exam_view(request):
    courseForm=QFORM.CourseForm()
    if request.method=='POST':
        courseForm=QFORM.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request,'teacher/teacher_add_exam.html',{'courseForm':courseForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_exam.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def delete_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')

@login_required(login_url='teacherlogin')
def teacher_question_view(request):
    return render(request,'teacher/teacher_question.html')

@login_required(login_url='teacherlogin')
def teacher_participantinfo_view(request):
    return render(request,'teacher/teacher_participantinfo.html')

@login_required(login_url='teacherlogin')
def teacher_thanks_view(request):
    return render(request,'teacher/teacher_thankyou.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_question_view(request):
    questionForm=QFORM.QuestionForm()
    if request.method=='POST':
        questionForm=QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request,'teacher/teacher_add_question.html',{'questionForm':questionForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_shortquestion_view(request):
    shortQuestionForm=QFORM.ShortQuestionForm()
    if request.method=='POST':
        shortQuestionForm=QFORM.ShortQuestionForm(request.POST)
        if shortQuestionForm.is_valid():
            question=shortQuestionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request,'teacher/teacher_add_shortanswer.html',{'shortQuestionForm':shortQuestionForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_participantinfo_view(request):
    infoForm=QFORM.InfoForm()
    if request.method=='POST':
        infoForm=QFORM.InfoForm(request.POST)
        if infoForm.is_valid():
            info=infoForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            info.course=course
            info.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-participantinfo')
    return render(request,'teacher/teacher_add_participantinformation.html',{'infoForm':infoForm})

def teacher_add_thanks_view(request):
    thanksForm=QFORM.ThanksForm()
    if request.method=='POST':
        thanksForm=QFORM.ThanksForm(request.POST)
        if thanksForm.is_valid():
            thankyou=thanksForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            thankyou.course=course
            thankyou.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-thanks')
    return render(request,'teacher/teacher_add_thanks.html',{'thanksForm':thanksForm})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_question_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_question.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_participantinfo_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_participantinfo.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_thanks_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'teacher/teacher_view_thanks.html',{'courses':courses})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_question_view(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_question.html',{'questions':questions})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_participantinfo_view(request,pk):
    info=QMODEL.Info.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_participantinfo.html',{'info':info})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_thanks_view(request,pk):
    thankyou=QMODEL.Thanks.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_thanks.html',{'thankyou':thankyou})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_shortanswer_view(request,pk):
    shortanswer=QMODEL.ShortQuestion.objects.all().filter(course_id=pk)
    return render(request,'teacher/see_shortanswer.html',{'shortanswer':shortanswer})

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_question_view(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')
    
@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_shortquestion_view(request,pk):
    shortquestion=QMODEL.ShortQuestion.objects.get(id=pk)
    shortquestion.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_info_view(request,pk):
    info=QMODEL.Info.objects.get(id=pk)
    info.delete()
    return HttpResponseRedirect('/teacher/teacher-view-participantinfo')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_thanks_view(request,pk):
    thanks=QMODEL.Thanks.objects.get(id=pk)
    thanks.delete()
    return HttpResponseRedirect('/teacher/teacher-view-thanks')