# Generated by Django 2.2.2 on 2020-01-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
