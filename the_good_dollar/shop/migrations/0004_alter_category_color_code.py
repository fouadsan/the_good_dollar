# Generated by Django 3.2.6 on 2021-08-17 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_title_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.color'),
        ),
    ]