# Generated by Django 3.2.8 on 2021-10-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('content', models.TextField(max_length=500)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]