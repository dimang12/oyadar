from django.shortcuts import render
import json
from django.core import serializers
from django.http import Http404, HttpResponse
from oyadar.models import Assignment, AssigmentQuestion, AssignmentAnswer



def index(request):
    # if request.user.is_authenticated():
    #     print("Hello")

    assignments = Assignment.objects.all()
    return render(
        request,
        "oyadar/assigments/index.html",
        {'assignments': assignments}
    )

def detail(request, id):

    # return HttpResponse(id)

    # try:
        questions = AssigmentQuestion.objects.all().order_by("ordering").filter(assignment_id=id)
        print(questions)

        cur_question = checkCurrentQuestion(questions)["cur_question"]


        # return HttpResponse("exit")
        answers = AssignmentAnswer.objects.all().filter(question_id=cur_question.id)
        status = checkCurrentQuestion(questions)
        return render(
            request,
            "oyadar/assigments/detail.html",
            {
                "question": cur_question,
                "status": status,
                "answers": answers
             }
        )
    # except:
        # raise Http404("The item does not exist.")



def checkCurrentQuestion(questions):
    order = 0
    isFinished = True
    object = {}
    for q in questions:
        if q.answer_id == 0:
            isFinished = False
            object["cur_question"] = questions[order]
            object["cur_order"] = order
            if len(questions) > 1:
                if order > 0:
                    object["prev_question"] = questions[order - 1].id
                if order < (len(object) - 1):
                    object["next_question"] = questions[order + 1].id
            else:
                object["prev_question"] = q.id
                object["next_question"] = q.id
            break
        order += 1

    if isFinished == True:
        object["cur_order"] = len(questions)
        object["cur_question"] = questions[len(questions)-1]
        object["prev_question"] = questions[len(questions)-2].id
    return object

# url: /answer/question-id
def chooseAnswer(request, id):
    # try:
        cur_dict = {}
        answer = AssignmentAnswer.objects.get(pk=id)
        AssigmentQuestion.objects.filter(id=answer.question_id_id).update(answer_id=id)

        questions = AssigmentQuestion.objects.all().order_by("ordering")

        cur = checkCurrentQuestion(questions)

        cur_dict["id"] = cur["cur_question"].id
        cur_dict["question_detail"] = cur["cur_question"].question_detail
        answers = AssignmentAnswer.objects.filter(question_id_id=cur["cur_question"].id).order_by("ordering")
        #

        # transfer to dictionary type
        cur["cur_question"] = cur_dict
        cur["answers"] = serializers.serialize("json",answers)
        # cur["answers"] = answerDict

        return HttpResponse(json.dumps(cur), content_type="application/json")
        # return render(request, "q")
    # except:
    #     return HttpResponse("Error")

def nextPrev(request, id):
    question = AssigmentQuestion.objects.get(pk=id)
    answers = AssignmentAnswer.objects.filter(question_id_id=id)

    questions = AssigmentQuestion.objects.filter(assignment_id_id=question.assignment_id_id).order_by("ordering")


    print(questions)

    # find current position of question
    order = 0
    cur_position = 1
    next_position = 0
    prev_position = 0
    status = {}

    for q in questions:

        if q.id == int(id):
            cur_position = order + 1
            if(order == 0 and len(questions)>1):
                # status["next_question"] = questions[cur_position + 1].id
                status["prev_question"] = questions[order].id
                # next_position = questions[order-1].objects
            if(order > 0 and order < len(questions)-1 ):
                status["next_question"] = questions[cur_position].id
                status["prev_question"] = questions[order-1].id
            else:
                status["next_question"] = q.id
                if(order > 0):
                    status["prev_question"] = questions[order-1].id
                else:
                    status["prev_question"] = questions[order].id

        order += 1



    return render(
                request,
                "oyadar/assigments/question-answer.html",
                {
                    "question": question,
                    "answers": answers,
                    "num_questions": len(questions),
                    # "status": checkCurrentQuestion(questions),
                    "status": status,

                    "cur_position": cur_position,
                    "next_position": next_position
                }
            )

def prev(request, id):
    question = AssigmentQuestion.objects.get(pk=id)
    answers = AssignmentAnswer.objects.filter(question_id_id=id)

    questions = AssigmentQuestion.objects.filter(assignment_id_id=question.assignment_id_id).order_by("ordering")

    print(questions)

    # find current position of question
    order = 0
    cur_position = 1
    next_position = 0
    prev_position = 0
    status = {}

    for q in questions:

        if q.id == int(id):
            cur_position = order + 1
            if (order == 0 and len(questions) > 1):
                # status["next_question"] = questions[cur_position + 1].id
                status["prev_question"] = questions[order].id
                next_position = questions[cur_position].objects
                # prev_position =
            else:
                status["next_question"] = questions[cur_position].id
                status["prev_question"] = questions[cur_position - 1].id
        order += 1

    return render(
        request,
        "oyadar/assigments/question-answer.html",
        {
            "question": question,
            "answers": answers,
            "num_questions": len(questions),
            # "status": checkCurrentQuestion(questions),
            "status": status,

            "cur_position": cur_position,
            "next_position": next_position
        }
    )

