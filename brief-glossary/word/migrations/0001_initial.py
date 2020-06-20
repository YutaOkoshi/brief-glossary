# Generated by Django 3.0.7 on 2020-06-20 11:03

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('glossary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', django_mysql.models.JSONField(default=dict, verbose_name='名前')),
                ('deleted', models.DateTimeField(null=True, verbose_name='削除日')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('created_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_user_id', to='user.User')),
                ('deleted_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_user_id', to='user.User')),
                ('glossary_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glossary.Glossary')),
                ('modified_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_user_id', to='user.User')),
            ],
        ),
    ]
