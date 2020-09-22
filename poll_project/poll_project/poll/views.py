from django.shortcuts import render,redirect
from .models import Poll
from .forms import CreatePollForm
def home(request):
    polls=Poll.objects.all()
    context={
        'polls':polls}
    return render (request,'poll/home.html',context)
def create(request):

    if request.method == "POST":
      form=CreatePollForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('home')
    else:
        form=CreatePollForm()
    context={'form':form}
    return render(request, 'poll/create.html', context)

def vote(request,pollid):
    p=Poll.objects.get(pk=pollid)
    if request.method=="POST":
        selectop=request.POST['pp']
        if selectop == 'option1':
            p.option_one_count+=1
        if selectop == 'option2':
            p.option_two_count+=1
        if selectop == 'option3':
            p.option_three_count+=1
        p.save()
        return redirect('result',p.id)
    context={'p':p}
    return render(request, 'poll/vote.html', context)
def result(request,pollid):
    p = Poll.objects.get(pk=pollid)
    context = {'p': p}
    return render(request, 'poll/result.html', context)