from rest_framework.routers import SimpleRouter
from api.users import views as users_api_views
from api.books import views as books_api_views
from api.purchases import views as purchase_api_views

router = SimpleRouter()

router.register('users', users_api_views.UserModelViewSet)
urlpatterns = router.urls

router.register('books', books_api_views.BookModelViewSet)
urlpatterns += router.urls

router.register('purchases', purchase_api_views.PurchaseModelViewSet)
urlpatterns += router.urls
