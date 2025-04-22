from django.urls import path

from tasks import views


urlpatterns = [
  path('', views.index, name='index'),

  path('signup/', views.signup_view, name='signup'),
  path('signin/', views.signin, name='signin'),
  path('signout/', views.signout, name='signout'),

  path('performers/', views.performers, name='performers'),
  path('performer/<int:performers_id>/', views.performer, name='performer'),
  path('create_user/', views.performers, name='create_user'),

  path('projects/', views.projects, name='projects'),
  path('projects/create/', views.create_project, name='projects_create'),
  path('project/<int:project_id>/', views.project, name='project'),

  path('tasks/', views.tasks, name='tasks'),
  path('tasks/create/', views.create_task, name='tasks_create'),
  path('tasks/<int:task_id>/', views.task, name='task'),
  
  
]