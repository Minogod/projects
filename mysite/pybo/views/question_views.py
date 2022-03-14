from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..forms import AnswerForm, CommentForm, QuestionForm
from ..models import Answer, Comment, Question

# @login_required 어노테이션은 login_url='common:login' 처럼 로그인 URL을 지정할 수 있다.
# Create your views here.





@login_required(login_url='common:login')
def question_create(request):
    """
    질문등록
    """
    if request.method == 'POST': # 요청값이 get 인지 post 인지 구분 
        form = QuestionForm(request.POST) # 받은 값 을 QuestionForm 인자에 넣어서 form 변수로 지정
        if form.is_valid(): # 폼이 유효한지 검사 vaild = 확인  
            question = form.save(commit=False) # form 이 유효하다면 아직 create_date가 비여있어서 바로 save를 할수없다 commit(기록)=False는 임시저장을 의미한다
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now() # question의 필수요소 3번째 인자 create_date를 입력하고
            question.ip = request.META['REMOTE_ADDR'] # IP받기?
            question.save() # save한다.
            return redirect('pybo:index') # render 와 redirect 차이 : redirect 는 변수를 html로 보낼수없다 그냥 경로지정만 가능 
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)
    # render 모듈 context 인자를 dictionary 형태로 보내주는데 
    # 함수 내에서 따로 지정안하고 바로 적어둔형태
    # html에서 {{key값 }}을 입력하면 value 값으로 보인다. 즉 key 값 form = value 값  form 이라 함수 변수 form = QuestionForm()이 되게된다. 
    # 여기서 변수 QuestionForm()은 mysite/forms.py 에서 import 된 QuestionForm 이다



@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')
