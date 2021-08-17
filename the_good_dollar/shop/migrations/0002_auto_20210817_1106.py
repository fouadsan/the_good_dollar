# Generated by Django 3.2.6 on 2021-08-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='departement',
        ),
        migrations.AddField(
            model_name='category',
            name='color_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='depart_imgs/'),
        ),
        migrations.DeleteModel(
            name='Departement',
        ),
    ]
