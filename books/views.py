from rest_framework import viewsets
from books.models import Book, Author, Member, BorrowRecord
from books.serializers import BookSerializer, AuthorSerializer, MemberSerializer, BorrowRecordSerializer
from rest_framework.permissions import IsAuthenticated
from books.permissions import IsLibrarian, IsMember,IsAdmin

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAuthenticated, IsLibrarian | IsAdmin]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAuthenticated, IsLibrarian | IsAdmin]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsLibrarian  | IsAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAuthenticated, IsLibrarian | IsAdmin]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsAdmin | IsLibrarian]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated, IsMember | IsLibrarian | IsAdmin] 
        elif self.action in ['update', 'destroy']:
            permission_classes = [IsAuthenticated, IsLibrarian] 
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]  
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    
    