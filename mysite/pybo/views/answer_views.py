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
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question,pk= question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)  
    # 인자로 받은 요청,질문 id값 
    # 질문 = 질문번호가있으면 질문번호 = 질문 , 없으면 404에러 /
    # 답변 = 데이터베이스 답변 (질문 = 질문, 내용 = http에서 받은요청값.post 에서 'content'값을 content로 설정 , 시간 = timzone 지금시간  )
    # 답변저장
    #  return  redirect = 다시보낸다 'pybo:detail, question_id = question_id'를  
    # 여기서 pybo:detail = [설정해둔 app명별칭]:[url 별칭],이다 결국  http://localhost:8000/pybo/ + question_id 값의 url이 다시 보내진다 는 것



@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)
