# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import School

def index(request):
    school_list = School.objects.all()
    template = loader.get_template('index.html')
    context = {
        'school_list': school_list,
    }
    return HttpResponse(template.render(context, request))

"""
# 快捷方式：render()
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""


# 每个视图至少做两件事之一：返回一个包含请求页面的HttpResponse对象或者弹出一个类似Http404的异常
def school_detail(request, school_id):
    school = School.objects.filter(id=school_id)
    res_text = school.name + " " + school.city + " " + school.area
    return HttpResponse(res_text)
