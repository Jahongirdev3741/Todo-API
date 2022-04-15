from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Todo(models.Model):
  NEW='new'
  FINISHED='finished'
  STATUS=(
    (NEW,'new'),
    (FINISHED,'finished')
  )
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='todos')
  title=models.CharField(max_length=128)
  body=models.TextField()
  status=models.CharField(max_length=8,choices=STATUS,default=NEW)

  def __str__(self) -> str:
    return self.title

  def mark_as_finished(self):
    self.status=self.FINISHED
    self.save()
  
  def mark_as_unfinished(self):
    self.status=self.NEW
    self.save()
