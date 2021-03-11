# Generated by Django 3.1.7 on 2021-03-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='images')),
                ('price', models.CharField(default='3500', max_length=20)),
                ('tag', models.CharField(choices=[('SY', 'Superyachts'), ('OS', 'Offshore'), ('SS', 'Safety and Security'), ('SG', 'Surveying'), ('SP', 'Shipping'), ('BR', 'Building and Repair')], default='SS', max_length=20)),
                ('duration', models.CharField(default='30', max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
