# Generated by Django 4.0.4 on 2022-06-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_job_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]