# Generated by Django 4.0.4 on 2022-06-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=30)),
                ('age', models.IntegerField(verbose_name=3)),
            ],
        ),
    ]