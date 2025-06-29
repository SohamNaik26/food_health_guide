# Generated by Django 5.2.2 on 2025-06-08 08:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='dietplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diet_plans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exerciseplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_plans', to=settings.AUTH_USER_MODEL),
        ),
    ]
