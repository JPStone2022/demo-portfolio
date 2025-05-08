from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_me_view, name='about_me'),
    path('projects/', views.all_projects_view, name='all_projects'),
    # Allow either slug or int for project detail for flexibility with static_data
    path('projects/<str:project_slug_or_id>/', views.project_detail_view, name='project_detail'),
    path('skills/', views.skill_list_view, name='skill_list'),
    path('demos/', views.all_demos_list_view, name='all_demos_list'),
    path('demos/<str:demo_slug_or_id>/', views.demo_detail_view, name='demo_detail'),
    path('topics/', views.topic_list_view, name='topic_list'),
    path('certificates/', views.certificates_view, name='certificates'),
    path('contact/', views.contact_view, name='contact'),
    path('search/', views.search_results_view, name='search_results'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('accessibility/', views.accessibility_view, name='accessibility'),
    path('terms/', views.terms_view, name='terms'),
    path('colophon/', views.colophon_view, name='colophon'),
    path('cv/', views.cv_view, name='cv'),
    path('hire-me/', views.hire_me_view, name='hire_me'),
    path('recommendations/', views.recommendation_list_view, name='recommendation_list'),
]
