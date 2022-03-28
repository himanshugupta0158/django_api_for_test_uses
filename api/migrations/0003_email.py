# Generated by Django 4.0.3 on 2022-03-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_phone_email_alter_phone_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256, verbose_name='Receiver Email')),
                ('subject', models.CharField(max_length=256, verbose_name='Subject')),
                ('body', models.CharField(max_length=1500, verbose_name='Body')),
            ],
        ),
    ]