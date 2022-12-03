# Generated by Django 4.1.3 on 2022-12-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_student_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='remaining_amount',
            field=models.IntegerField(default=15000),
        ),
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]