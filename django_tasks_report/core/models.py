from django.db import models
from django.contrib.auth.models import User


class Setting(models.Model):
    id_user = models.ForeignKey(User, blank=True, null=True, verbose_name='User')
    shift_start_time = models.TimeField(blank=True, null=True, verbose_name='Shift Start Time')
    shift_end_time = models.TimeField(blank=True, null=True, verbose_name='Shift End Time')

    def __str__(self):
        return User.objects.get(id=self.id_user).get_full_name()


class Repository(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')  # name (repository[name])
    url = models.URLField(max_length=255, verbose_name='Url')  # url (repository[owner][html_url])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')

    def __str__(self):
        return self.name


class Commit(models.Model):
    id_user = models.ForeignKey(User, blank=True, null=True, verbose_name='User')
    message = models.TextField(verbose_name='Message')  # message (commits[message])
    end_datetime = models.DateTimeField(verbose_name='Finished')  # end_datetime (commits[timestamp])
    start_datetime = models.DateTimeField(blank=True, null=True, verbose_name='Started')
    url = models.URLField(max_length=255, verbose_name='Url')  # url (commits[url])
    reported = models.BooleanField(default=False, verbose_name='Reported')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Category')
    repository = models.ForeignKey(Repository, verbose_name='Repository')

    def __str__(self):
        return self.message
