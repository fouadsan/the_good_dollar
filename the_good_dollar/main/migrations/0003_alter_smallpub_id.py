# Generated by Django 3.2.6 on 2021-09-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210929_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallpub',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
