# Generated by Django 4.0.4 on 2022-06-02 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
