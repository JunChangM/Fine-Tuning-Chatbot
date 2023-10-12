from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Permission_classes = [IsAuthenticated] # 인증된 사용자만 해당 뷰셋의 엔드포인트에 접근할 수 있습니다. 9장에서 이어서 진행
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['publication_date', 'price']
    
    def get_queryset(self):
        # 사용자 정의 필터링 및 정렬 로직을 여기에 구현합니다.
        # 요청에서 필터링 매개변수를 가져옵니다 (예: 쿼리 매개변수).
        # 매개변수를 기반으로 쿼리셋에 필터링 및 정렬을 적용합니다.
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        
        ordering = self.request.query_params.get('ordering', None)
        if ordering in self.ordering_fields:
            queryset = queryset.order_by(ordering)

        return queryset
    


@api_view(['POST','GET'])
def create_book(request):
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


