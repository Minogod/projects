from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm
# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date') # order_by = 정령 
    context = {'question_list':question_list}
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


def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question,pk= question_id)
    answer = Answer(question = question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id = question_id)
    # 인자로 받은 요청,질문 id값 
    # 질문 = 질문번호가있으면 질문번호 = 질문 , 없으면 404에러 /
    # 답변 = 데이터베이스 답변 (질문 = 질문, 내용 = http에서 받은요청값.post 에서 'content'값을 content로 설정 , 시간 = timzone 지금시간  )
    # 답변저장
    #  return  redirect = 다시보낸다 'pybo:detail, question_id = question_id'를  
    # 여기서 pybo:detail = [설정해둔 app명별칭]:[url 별칭],이다 결국  http://localhost:8000/pybo/ + question_id 값의 url이 다시 보내진다 는 것

def question_create(request):
    """
    질문등록
    """
    form = QuestionForm()
    return render(request, 'pybo/question_form.html',{'form':form})
    # render 모듈 context 인자를 dictionary 형태로 보내주는데 
    # 함수 내에서 따로 지정안하고 바로 적어둔형태
    # html에서 {{key값 }}을 입력하면 value 값으로 보인다. 즉 key 값 form = value 값  form 이라 함수 변수 form = QuestionForm()이 되게된다. 
    # 여기서 변수 QuestionForm()은 mysite/forms.py 에서 import 된 QuestionForm 이다
    # 