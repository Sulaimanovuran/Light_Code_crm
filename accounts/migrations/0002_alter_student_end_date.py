# Generated by Django 4.1.3 on 2022-11-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='end_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
