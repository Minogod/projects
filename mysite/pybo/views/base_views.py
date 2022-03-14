from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..forms import AnswerForm, CommentForm, QuestionForm
from ..models import Answer, Comment, Question

# @login_required 어노테이션은 login_url='common:login' 처럼 로그인 URL을 지정할 수 있다.
# Create your views here.


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    #get방식으로 호출된 url 에서 page 값을 받아옴 디폴트값 1로지정

    # 조회
    question_list = Question.objects.order_by('-create_date') # order_by = 정령 

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    # Paginator
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    # context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html',context) 
    # render(request,template_name,context=None, content_type=None, status=None, using=None)
    # 여기서 request 와 template_name 은 필수인자로 받아야한다
    # context 변수를 html 파일에 인자로 넘겨줘서 html파일에서 변수를 사용할수있다.
    # context 는 딕셔너리형으로 사용하며 key 값이 탬플릿에서 사용할 변수이름, value 값이 파이썬 변수

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
