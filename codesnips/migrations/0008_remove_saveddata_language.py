# Generated by Django 3.2.8 on 2021-11-09 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codesnips', '0007_auto_20211109_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saveddata',
            name='language',
        ),
    ]