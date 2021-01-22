# Generated by Django 2.2 on 2021-01-20 13:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question_app', '0006_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='contestent_answer',
            field=models.CharField(choices=[('S', 'S'), ('W', 'W'), ('R', 'R')], help_text='Enter right answer - Skip,Right,Wrong', max_length=1),
        ),
        migrations.AlterUniqueTogether(
            name='attempt',
            unique_together={('contestent', 'contestent_question')},
        ),
    ]
