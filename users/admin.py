from django.contrib import admin
from users.models import CustomUser
from books.models import Book,BorrowRecord,Author,Member
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(BorrowRecord)
admin.site.register(Author)
admin.site.register(Member)

