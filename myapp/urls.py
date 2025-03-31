from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomPasswordResetView
urlpatterns = [
   path('',views.index, name='index'),
   path('user',views.user, name='user'),
   path('signin',views.signin, name='signin'),
   path('signup',views.signup, name='signup'),
   path('install',views.install,name='install'),
   path('transactions',views.transactions,name='transactions'),
   path('backup',views.backupt,name='backup'),
   path('backuph',views.backuph,name='backuph'),
   path('withdraw',views.withdraw,name='withdraw'),
   path('whistory',views.whistory,name='whistory'),
   path('coinswap',views.coinswap,name='coinswap'),
   path('bckwh',views.bckwh,name='bckwh'),
   path('bh',views.bh,name='bh'),
   path('nfts',views.nfts,name='nfts'),
   path('userupd',views.userupd,name='userupd'),
   path('buy_nft', views.buy_nft, name='buy_nft'),
   path('sell_nft', views.sell_nft, name='sell_nft'),
   path('mynft',views.mynft,name='mynft'),
   path('lw',views.lw,name='lw'),
   path('con_w/<str:id>',views.conw,name='con_w'),
   path('card',views.card,name='card'),
   path('myprofile',views.myprofile,name='myprofile'),
   path('profup/<str:id>',views.profup,name='profup'),
   path('kycver',views.kycver,name='kycver'),
   path('buyc',views.buyc,name='buyc'),
   path('logout',views.logout,name='logout'),
   path('generate_ref_link',views.generate_ref_link,name='generate_ref_link'),
   path('fundsr',views.fundsr,name='fundsr'),
   path('cardpayment',views.cardpayment,name='cardpayment'),
   path('cardspayment/<str:id>',views.cardspayment,name='cardspayment'),
   path('mycards',views.mycards,name='mycards'),
   path('humindex',views.humindex,name='humindex'),
   path('charitypay/<str:id>',views.charitypay,name='charitypay'),
   path('chargiftc',views.chargiftc,name='chargiftc'),
   path('mydano',views.mydano,name='mydano'),
   path('medbed',views.medbedhome,name='medbed'),
   path('cartapply',views.cartapply,name='cartapply'),
   path('veri_page',views.veri_page,name='veri_page'),
   path('home',views.home,name='home'),
   path('a',views.a,name='a'),
   path('trbp',views.trbp,name='trbp'),



   # Password reset URLs
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
# admin012


# bkdb
# pass = 9387$##THus75


# admin@mail.com
# myPASS1122