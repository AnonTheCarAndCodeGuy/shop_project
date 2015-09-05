from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shop_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^login/', views.LoginView.as_view(), name="login"),
    url(r'^carlot/', views.CarlotView.as_view(), name="carlot"),
    url(r'^about/', views.AboutView.as_view(), name="about"),
    url(r'^faq/', views.FaqView.as_view(), name="faq"),
    url(r'^dashboard/', views.DashboardView.as_view(), name="dashboard"),
    url(r'^register/', views.RegisterView.as_view(), name="register"),
    url(r'^profile/', views.ProfileView.as_view(), name="profile"),
    url(r'^logout/', views.LogoutView.as_view(), name="logout"),
    url(r'^addcar/', views.AddcarView.as_view(), name="addcar"),
    url(r'^cardetail/(?P<car_id>\w+)/detail',views.CardetailView.as_view(car_id=None), name='cardetail'),
    url(r'^addbrand/', views.AddbrandView.as_view(), name="addbrand"),
    url(r'^mycars/(?P<owner_id>\w+)/all', views.MycarsView.as_view(owner_id=None), name="mycars"),
)

