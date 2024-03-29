# Generated by Django 2.0.7 on 2019-12-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=0.0, max_length=30),
            preserve_default=False,
        ),
    ]
