from django.urls import path
from . import views 


from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('index/', views.Index, name="index"),
    path('rIndex/', views.rIndex, name="rIndex"),
    path('AddNews', views.AddNews, name="AddNews"),
    path('SaveNews', views.SaveNews, name="SaveNews"),
    path('ShowAllNews', views.ShowAllNews, name="ShowAllNews"),
    path('EditReport/<int:note_id>', views.EditReport, name="EditReport"),
    path('update/', views.update, name="update"),
    path('delete/<int:note_id>', views.delete, name="delete"),

    path('AprroveNews/<int:note_id>', views.AprroveNews, name="AprroveNews"),
    path('', views.userNews, name="userNews"),
    path('singlePage/<int:note_id>', views.singlePage, name="singlePage"),



    path('adminLogin', views.adminLogin, name="adminLogin"),
    path('adminIndex', views.adminIndex, name="adminIndex"),

    path('reporterLogin', views.reporterLogin, name="reporterLogin"),
    path('reporterIndex', views.reporterIndex, name="reporterIndex"),

    path('Logout', views.Logout, name="Logout"),


    path('ReporterNews', views.ReporterNews, name="ReporterNews"),

    path('register', views.register, name="register"),
    path('ReporterRegister', views.ReporterRegister, name="ReporterRegister"),
    path('ShowAllreporter', views.ShowAllreporter, name="ShowAllreporter"),
    path('yourProfile', views.yourProfile, name="yourProfile"),

    path('memberAprrove/<int:note_id>', views.memberAprrove, name="memberAprrove"),
    path('EditProfile/<int:note_id>', views.EditProfile, name="EditProfile"),
    path('ProfileUpdate/', views.ProfileUpdate, name="ProfileUpdate"),

    path('sendEmail/<int:note_id>', views.sendEmail, name="sendEmail"),
    path('verifiedAcc', views.verifiedAcc, name="verifiedAcc"),

    path('ApprovedNews', views.ApprovedNews, name="ApprovedNews"),
    path('SendVerifyEmail', views.SendVerifyEmail, name="SendVerifyEmail"),

    path('userExist', views.userExist, name="userExist"),
    path('updateVerifyStatus', views.updateVerifyStatus, name="updateVerifyStatus"),

]
urlpatterns += staticfiles_urlpatterns()