from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

# 템플릿 필터 함수를 만드는 방법은 무척 간단하다. 위처럼 sub 함수에 @register.filter 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있게 된다.

# sub 필터는 기존 값 value에서 입력으로 받은 값 arg를 빼서 리턴한다.