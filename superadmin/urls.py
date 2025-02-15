from django.urls import path
from . import views
from .views import login_as_user

urlpatterns = [
    path('',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('lw',views.lw,name='lw'),
    path('deposit',views.deposit,name='deposit'),
    path('depinfo/<str:id>',views.depinfo,name='depinfo'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('withinfo/<str:id>',views.withinfo,name='withinfo'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('backupt',views.backupt,name='backupt'),
    path('backupinfo/<str:id>',views.backupinfo,name='backupinfo'),
    path('backupw',views.backupw,name='backupw'),
    path('backupwinfo/<str:id>',views.backupwinfo,name='backupwinfo'),
    path('addf',views.addf,name='addf'),
    path('userkyc',views.userkyc,name='userkyc'),
    path('userkyc_view/<str:id>',views.userkyc_view,name='userkyc_view'),
    path('adds',views.adds,name='adds'),
    path("admin/login-as-user/<int:user_id>/", login_as_user, name="login_as_user"),
    # path("user/dashboard/<int:user_id>/", user_dashboard, name="user_dashboard"),
    path('addb',views.addb,name='addb'),
    path('addbs',views.addbs,name='addbs'),
    path('read/<str:id>',views.read,name='read'),
    path('add_nft',views.add_nft,name='add_nft'),
    path('setting',views.setting,name='setting'),
    path('cardmake',views.cardmake,name='cardmake'),
    path('cardhis',views.cardhis,name='cardhis'),
    path('cardde/<str:id>',views.cardde,name='cardde'),
    path('alluser',views.alluser,name='alluser'),
]