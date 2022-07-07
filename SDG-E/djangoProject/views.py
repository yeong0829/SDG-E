from django.shortcuts import render, redirect

# 게시판 추가 구현
from .forms import *
from .models import *

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        board = Board(
            title=title,
            content=content,
            writer=writer,
        )
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'board.html', context)


# 게시판 수정 구현
def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.writer = request.POST['writer']

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'update.html', {'boardForm':boardForm})


# 게시판 삭제 구현
def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')