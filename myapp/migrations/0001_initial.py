# Generated by Django 4.2.3 on 2024-01-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
