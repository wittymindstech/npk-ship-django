# Generated by Django 3.1.7 on 2021-03-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knotend', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='rzr_pay_id',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]