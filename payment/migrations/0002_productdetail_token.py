# Generated by Django 4.2.6 on 2023-10-08 15:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
