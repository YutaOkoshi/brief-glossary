from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils import timezone
# from django_mysql.models import JSONField


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    name = models.CharField(
        verbose_name='名前',
        max_length=100
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=255
    )
    memo = models.TextField(
        verbose_name='メモ',
        null=True,
        blank=True,
    )
    deleted = models.DateTimeField(
        verbose_name='削除日',
        null=True,
        blank=True,
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

# TODO: ユーザー変更履歴を見れるようにしたい


class GlossaryUser(models.Model):
    class Meta:
        db_table = 'glossary_user'

    ROLE_ADMIN = 1
    ROLE_NOMAL = 2
    ROLE_READONLY = 3

    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Admin'),
        (ROLE_NOMAL, 'Nomal'),
        (ROLE_READONLY, 'ReadOnly')
    )

    glossary_id = models.ForeignKey(
        'glossary.Glossary',
        on_delete=models.CASCADE,
    )
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    role_id = models.IntegerField(
        'Role',
        choices=ROLE_CHOICES
    )
    deleted = models.DateTimeField(
        verbose_name='削除日',
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name='作成日',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name='更新日',
        auto_now=True
    )
