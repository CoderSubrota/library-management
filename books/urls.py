from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, AuthorViewSet, MemberViewSet, BorrowRecordViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Schema view for Swagger and ReDoc documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Library Management API",
        default_version='v1',
        description="API documentation for the Library Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@library.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

# Setting up the router for viewsets
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrow', BorrowRecordViewSet)

# URL patterns
urlpatterns = [
    path('auth/', include('djoser.urls')),  # Djoser authentication URLs
    path('auth/', include('djoser.urls.jwt')),  # Djoser JWT URLs
    path('auth/auth/users/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh
    path('auth/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),  # JWT verify
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),  # ReDoc UI
    path('', include(router.urls)),  # Include the router URLs
]