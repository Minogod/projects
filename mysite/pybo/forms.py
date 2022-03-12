from django import forms
from pybo.models import Question

#  form 은 페이지 요청시 전달되는 파라미터 들을 쉽게 관리하기 위해 사용하는 클래스이다.
# 폼은 필수 파라미터의 값이 누락되지않았는지 적절한지등 검증할 목적으로 사용한다.
# 이외에도 HTML을 자동으로 생성하거나 폼에 연결된 모델을 이용하여 데이터를 저장할수도있다 .


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
        'subject': '제목',
        'content': '내용',
        }  
        

# 장고 formdms dlfqksvha (forms.Form)과 모델폼(forms.ModelForm)이 있다.
# 모델폼은 모델과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할수 있는 폼이다.
# 모델폼은 이너클래스인 Meta클래스가 반드시 필요하다. Meta 클래스에는 사용할 모델과 모델의 속성을 적어야한다.

# widgets을 추가하여 
# attrs = attribute(속성)의 약어
# 부스트트랩 클래스를 이용할수있다. 어떻게 ??
