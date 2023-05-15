from django.http import HttpResponse
from .models import Question



def pollsindex(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    # return HttpResponse("Polls index...")



def pollsdetail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)



def pollsresults(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)



def pollsvote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)