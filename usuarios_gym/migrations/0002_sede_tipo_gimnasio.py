# Generated by Django 5.0.6 on 2024-06-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_gym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sede',
            name='tipo_gimnasio',
            field=models.CharField(choices=[('prime', 'Prime'), ('plus', 'Plus'), ('classic', 'Classic')], max_length=10, null=True),
        ),
    ]
