# Generated by Django 2.2.2 on 2020-01-07 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weigh_word', models.CharField(blank=True, max_length=40, null=True)),
                ('weigh_photo', models.ImageField(blank=True, null=True, upload_to='weight_photo')),
                ('body_photo', models.ImageField(blank=True, null=True, upload_to='body_photo')),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]