from django.urls import path

from tasks import views


urlpatterns = [
  path('', views.index, name='index'),
  path('projects/', views.projects, name='projects'),
  path('performers/', views.performers, name='performers'),
  path('tasks/', views.tasks, name='tasks'),
  path('projects/', views.projects, name='projects'),
  path('projects/create/', views.create_project, name='projects_create'),
  path('project/<int:project_id>/', views.project, name='project'),
  path('create_user/', views.create_user, name='create_user'),
  # path('tasks/', views.tasks, name='tasks'),
  path('tasks/create/', views.create_task, name='tasks_create'),
  path('tasks/<int:task_id>/', views.task, name='task'),
  path('signup/', views.signup_view, name='signup'),
  path('signin/', views.signin, name='signin'),
  path('signout/', views.signout, name='signout'),

]

#   path('projects/', views.projects, name='projects'),
#   path('project/<int:project_id>', views.project, name='project'),
#   path('create_project/', views.create_project, name='create_project'),
#   path('create_user/', views.create_user, name='create_user'),
#   path('create_task/', views.create_task, name='create_task'),
# ]