# Generated by Django 3.0.7 on 2020-06-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200620_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryuser',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='削除日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='削除日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='メモ'),
        ),
    ]
