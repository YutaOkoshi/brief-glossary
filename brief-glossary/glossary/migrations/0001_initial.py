# Generated by Django 3.0.7 on 2020-06-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='用語集名')),
                ('is_public', models.BooleanField(default=False, verbose_name='誰でも閲覧できるかどうか')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='削除日')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
            options={
                'db_table': 'glossary',
            },
        ),
    ]
