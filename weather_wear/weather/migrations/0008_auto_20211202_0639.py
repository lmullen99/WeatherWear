# Generated by Django 3.2.9 on 2021-12-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_outfit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='accessories',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='bottom',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='footwear',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='outerwear',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='top',
            field=models.CharField(max_length=40),
        ),
    ]
