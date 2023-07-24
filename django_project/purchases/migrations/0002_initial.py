# Generated by Django 4.2.3 on 2023-07-18 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_purchases', to=settings.AUTH_USER_MODEL),
        ),
    ]