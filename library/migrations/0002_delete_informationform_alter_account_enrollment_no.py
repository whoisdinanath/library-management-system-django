# Generated by Django 4.0.4 on 2022-05-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InformationForm',
        ),
        migrations.AlterField(
            model_name='account',
            name='enrollment_no',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]