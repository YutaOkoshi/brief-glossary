from django.db import models
from django.forms import ModelForm
# from django.utils import timezone
from django_mysql.models import JSONField
from django.core.exceptions import NON_FIELD_ERRORS


class Word(models.Model):
    class Meta:
        db_table = 'word'

    word = models.CharField(
        verbose_name='単語',
        max_length=255,
    )
    info = JSONField(
        verbose_name='属性',
    )
    glossary = models.ForeignKey(
        'glossary.Glossary',
        on_delete=models.CASCADE,
        related_name="glossary",
    )

    deleted = models.DateTimeField(
        verbose_name='削除日',
        null=True,
        blank=True,
    )
    deleted_user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name="deleted_user",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name='作成日',
        auto_now_add=True
    )
    created_user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name="created_user"
    )
    modified = models.DateTimeField(
        verbose_name='更新日',
        auto_now=True
    )
    modified_user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name="modified_user"
    )

    def __str__(self):
        return self.word

# TODO: 単語変更履歴を見れるようにしたい


class WordForm(ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model = Word
        fields = [
            'word',
            'info',
            'glossary',
        ]
