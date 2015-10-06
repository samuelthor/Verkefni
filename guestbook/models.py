import datetime
from django.db import models
from django.utils import timezone



class text(models.Model):
    title_text = models.CharField(max_length=200, blank=True)
    question_text = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):      # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
