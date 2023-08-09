from django.urls import path
from . import views


urlpatterns = [
    path('init/',views.InitializeWallet.as_view()),
    path('wallet/',views.EnableWallet.as_view()),
    path('wallet/transactions/',views.WalletTransaction.as_view({"get":"transactions"})),
    path('wallet/deposits/',views.WalletTransaction.as_view({"post":"deposits"})),
    path('wallet/withdrawals/',views.WalletTransaction.as_view({"post":"withdrawals"})),
]