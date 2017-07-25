# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.conf import settings

def min_length_3_validator(value):
    if len(value) < 3:
        raise ValidationError('3글자 이상 입력해주세요.')

class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField(help_text="MarkDown 문법을 지원합니다.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
