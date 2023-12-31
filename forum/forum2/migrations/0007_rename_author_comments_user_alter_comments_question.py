# Generated by Django 4.0.1 on 2022-11-02 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum2', '0006_alter_comments_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='comments',
            name='Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum2.question'),
        ),
    ]
