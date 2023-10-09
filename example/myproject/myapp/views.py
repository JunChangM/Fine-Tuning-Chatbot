from django.shortcuts import render, redirect
from .forms import BookForm
from myapp.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# Create your views here.

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Respose(serializer.errors,status=400)

    # if request.method == 'POST':
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('book_list')
    # else:
    #     form = BookForm()
    # return render(request, 'create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer