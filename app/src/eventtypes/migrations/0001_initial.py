# Generated by Django 2.2.6 on 2019-11-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventtype',
            fields=[
                ('type', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]