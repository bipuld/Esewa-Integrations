# Generated by Django 4.2.6 on 2023-10-07 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product')),
                ('service_charge', models.IntegerField()),
                ('detail', models.TextField()),
                ('price', models.IntegerField(default='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.product')),
            ],
        ),
    ]