# Generated by Django 2.0.7 on 2019-12-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20191211_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]