# Generated by Django 4.0.3 on 2022-03-13 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_question_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='ip',
        ),
    ]