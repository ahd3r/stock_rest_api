# Generated by Django 2.1.3 on 2018-11-12 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_api', '0002_auto_20181112_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmodel',
            name='hunter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
