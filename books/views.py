from rest_framework import viewsets
from books.models import Book, Author, Member, BorrowRecord
from books.serializers import BookSerializer, AuthorSerializer, MemberSerializer, BorrowRecordSerializer
from rest_framework.permissions import IsAuthenticated
from books.permission import IsLibrarian, IsMember

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAuthenticated, IsLibrarian]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsMember]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarian] 

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]  

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAuthenticated, IsLibrarian]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsMember]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    