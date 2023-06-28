# Generated by Django 4.0.1 on 2022-11-24 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum2', '0011_alter_comments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum2.question'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
