from django.urls import path 
from .views import(
    HomeView,
    MyLoginView,
    logoutUser,
    DeleteCardView,
    UpdateCardView,
    CreateCardView,
    activateCard,
    deactivateCard,
    TransactionListView
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('card/create/', CreateCardView.as_view(), name='create'),
    path('card/update/<int:pk>', UpdateCardView.as_view(), name='update'),
    path('card/delete/<int:pk>', DeleteCardView.as_view(), name='delete'),
    path('card/activate/<int:pk>', activateCard, name='activate'),
    path('card/deactivate/<int:pk>', deactivateCard, name='deactivate'),
    path('transactions/<int:pk>', TransactionListView.as_view(), name='card-transactions')
]