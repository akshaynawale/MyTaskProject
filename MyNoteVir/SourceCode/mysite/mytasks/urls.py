from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.login_page, name='login'),
        url(r'^create_account$', views.create_account_page,
            name='create_account'),
        url(r'^create_account_result$', views.create_account_result_page,
            name='create_account_result'),
        url(r'^home$', views.home_page, name='home'),
        url(r'^by_owner$', views.home_page_by_owner, name='by_owner'),
        url(r'^video_test$', views.video_test, name='video_test'),
        ]
