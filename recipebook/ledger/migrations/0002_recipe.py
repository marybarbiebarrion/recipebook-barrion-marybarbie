# Generated by Django 5.0.3 on 2024-03-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
