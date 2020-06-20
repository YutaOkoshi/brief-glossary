from django.db import models
from django.utils import timezone
# from django_mysql.models import JSONField


class Glossary(models.Model):
    class Meta:
        db_table = 'glossary'

    name = models.CharField(
        verbose_name='用語集名',
        max_length=100
    )
    is_public = models.BooleanField(
        verbose_name='誰でも閲覧できるかどうか',
        default=False,
    )
    deleted = models.DateTimeField(
        verbose_name='削除日',
        null=True,
    )
    created = models.DateTimeField(
        verbose_name='作成日',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name='更新日',
        auto_now=True
    )

    def __str__(self):
        return self.name
