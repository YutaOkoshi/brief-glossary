from django.db import models
from django.utils import timezone
from django_mysql.models import JSONField


class Word(models.Model):
    class Meta:
        db_table = 'word'

    info = JSONField(
        verbose_name='名前',
    )
    glossary_id = models.ForeignKey(
        'glossary.Glossary',
        on_delete=models.CASCADE,
    )

    deleted = models.DateTimeField(
        verbose_name='削除日',
        null=True
    )
    deleted_user_id = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name="deleted_user_id"
    )
    created = models.DateTimeField(
        verbose_name='作成日',
        auto_now_add=True
    )
    created_user_id = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name="created_user_id"
    )
    modified = models.DateTimeField(
        verbose_name='更新日',
        auto_now=True
    )
    modified_user_id = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name="modified_user_id"
    )

    def __str__(self):
        return self.name

# TODO: 単語変更履歴を見れるようにしたい

