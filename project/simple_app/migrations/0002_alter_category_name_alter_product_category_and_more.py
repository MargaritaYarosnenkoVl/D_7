# Generated by Django 4.0.4 on 2022-05-24 06:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_app.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >= 0')]),
        ),
    ]
