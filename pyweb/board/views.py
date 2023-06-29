from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.forms import QuestionForm, AnswerForm
from board.models import Question, Answer

def index(request):
    return render(request, 'board/index.html')
    #return HttpResponse("웹 메인페이지입니다.")

def question_list(request):
    question_list = Question.objects.order_by('-create_date')
    #페이지 처리
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list':page_obj}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST) #입력된 데이터가 있는 폼
        if form.is_valid(): #폼이 유효성 검사 통과
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            form.save()
            return redirect('board:question_list')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'board/question_form.html',context) #get 방식

@login_required(login_url='common:login')
def answer_create(request, question_id):
    # 질문이 1개 있어야 답변 등록이 가능
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            form.save()
            return redirect('board:detail',question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form':form}
    return render(request, 'board/detail.html',context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    # 수정을 위해 질문 가져옴
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('board:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:question_list')

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('board:detail', question_id=answer.question.id)