# Generated by Django 3.2.9 on 2021-12-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0011_alter_outfit_outerwear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='outerwear',
            field=models.CharField(max_length=40, null=True),
        ),
    ]