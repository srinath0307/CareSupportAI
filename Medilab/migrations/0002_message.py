# Generated by Django 4.2.3 on 2023-07-28 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medilab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('chat_type', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000000)),
            ],
        ),
    ]
