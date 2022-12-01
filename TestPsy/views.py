from django.shortcuts import render, redirect
from .models import Quests
from .counter import Counter


# Create your views here.
def main(request):
    if request.method == "GET":
        return render(request, 'main.html')


def questions(request):
    if request.method == "POST":
        number_quest = int(request.POST.get('quest')) + 1
        if number_quest <= 16:
            if number_quest == 1:
                request.session['data'] = {}
                request.session['data']['age'] = request.POST.get('age')
                request.session['data']['sex'] = request.POST.get('sex')
                request.session['data']['education'] = request.POST.get('education')
                request.session['data']['work'] = request.POST.get('work')
                request.session.modified = True
            else:
                request.session['data'][f'answer{str(number_quest - 1)}'] = request.POST.get('answer')
                request.session.modified = True
            quest = Quests.objects.get(number=number_quest)
            context = {'number_quest': number_quest, 'quest': quest}
            return render(request, 'questions.html', context=context)
        else:
            request.session['data'][f'answer{str(number_quest - 1)}'] = request.POST.get('answer')
            request.session.modified = True
            return redirect('final')
    pass


def final(request):
    data = request.session.get('data')
    data_with_only_answer = [value for key, value in data.items() if 'answer' in key]
    c = Counter(data)
    c.write_in_db()
    q = Quests.objects.all()
    count = 0
    for answer, right_answer in zip(data_with_only_answer, q):
        if answer == right_answer.right_answer:
            count += 1
    context = {'count': count}
    return render(request, 'final.html', context=context)
