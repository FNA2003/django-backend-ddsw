from django.db import models
import datetime

# Por defecto: null=False y blank=False
class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    previous_task_fd = models.ForeignKey("self",
                                         null=True,
                                         on_delete=models.SET_NULL)
    project_fk = models.ForeignKey("projects.Projects",
                                   on_delete=models.CASCADE,
                                   # related_name => Projects.objects.get(id=x).tasks...
                                   related_name="tasks")
    
    asigned_groups_fk = models.ManyToManyField("groups.Groups",
                                               blank=True,
                                               # related_name => Groups.objects.get(id=x).asigned_tasks_group.all()
                                               related_name="asigned_tasks_group")
    asigned_users_fk = models.ManyToManyField("users.Users",
                                              blank=True,
                                              # related_name => Users.objects.get(id=x).asigned_tasks_user.all()
                                              related_name="asigned_tasks_user")
    
    completed = models.BooleanField(default=False)
    limit_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(default=datetime.datetime.now)