# Generated by Django 4.2.17 on 2024-12-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('order_id', models.IntegerField()),
            ],
        ),
    ]
