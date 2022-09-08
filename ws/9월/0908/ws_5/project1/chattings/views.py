from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat
from .forms import ChattingForm
# Create your views here.

def index(request):
    chattings = Chat.objects.all()
    context = {
        'chattings':chattings,
    }
    return render(request, 'chattings/index.html', context)

def create(request):
    if request.method == 'POST':
        # create
        form = ChattingForm(request.POST)
        if form.is_valid():
            chatting = form.save()
            return redirect(f"/chattings/{chatting.pk}", chatting.pk)
        pass
    else:
        #new
        form = ChattingForm()
    context ={
        'form': form,
    }
    return render(request, 'chattings/create.html', context)


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    chatting =get_object_or_404(Chat, pk=pk)
   
    
    context = {
        'chatting': chatting,
    }
    return render(request, 'chattings/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        chatting = Chat.objects.get(pk=pk)
        chatting.delete()
    return redirect('chattings:index')