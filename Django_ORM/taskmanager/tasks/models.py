from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
  class Meta:
    verbose_name = 'проект'
    verbose_name_plural = 'проекты'

  name = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

  def __str__(self):
    return self.name


class User(AbstractUser):
  class Meta:
    verbose_name = 'пользователь'
    verbose_name_plural = 'пользователи'
   

  firstname = models.CharField(max_length=100, verbose_name='Имя')
  lastname = models.CharField(max_length=100, verbose_name='Фамилия')

  def __str__(self):
    return self.username


class TaskStatus(models.Model):
  class Meta:
    verbose_name = 'статус задачи'
    verbose_name_plural = 'статусы задачи'
  name = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')

  def __str__(self):
    return self.name


class Task(models.Model):
  class Meta:
    verbose_name = 'задача'
    verbose_name_plural = 'задачи'

  title = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')
  status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, verbose_name='Статус')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
  due_date = models.DateField(verbose_name='Срок выполнения')
  project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
  performers = models.ManyToManyField(User, verbose_name='Исполнители')
  comment = models.TextField(blank=True, verbose_name='Коментарий')

  def __str__(self):
    return f'{self.title} ({self.status})'

    
# class Project(models.Model):
#   name = models.CharField(max_length=100)
#   description = models.TextField()
#   created_at = models.DateTimeField(auto_now_add=True)
  
#   def __str__(self):
#       return self.name

# # class Executor(models.Model):
# #   name = models.CharField(max_length=100)
# #   email = models.EmailField()

# #   def __str__(self):
# #       return self.name

# # class User(models.Model):
# #   username = models.CharField(max_length=100)
# #   email = models.EmailField()
  
# #   def __str__(self):
# #       return self.username
# class User(AbstractUser):
#   firstname = models.CharField(max_length=100)
#   lastname = models.CharField(max_length=100)

#   def __str__(self):
#     return self.username


# class TaskStatus(models.Model):
#   name = models.CharField(max_length=100)
#   description = models.TextField()

#   def __str__(self):
#     return self.name



# class Task(models.Model):
#   title = models.CharField(max_length=100)
#   description = models.TextField()
#   status = models.ForeignKey(TaskStatus, on_delete=models.DO_NOTHING)
#   created_at = models.DateTimeField(auto_now_add=True)
#   due_date = models.DateField()
#   project = models.ForeignKey(Project, on_delete=models.CASCADE)
#   performers = models.ManyToManyField(User)
  
#   def __str__(self):
#       return f'{self.title} ({self.status})'


# Create your models here.
