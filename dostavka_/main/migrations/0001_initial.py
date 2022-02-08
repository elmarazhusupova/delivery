# Generated by Django 4.0.2 on 2022-02-03 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='Scale_weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='Dostavka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='amount')),
                ('length', models.IntegerField(verbose_name='length')),
                ('width', models.IntegerField(verbose_name='width')),
                ('height', models.IntegerField(verbose_name='height')),
                ('weight', models.IntegerField(verbose_name='weight')),
                ('total_price', models.IntegerField(default=0, verbose_name='total_price')),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.scale', verbose_name='scale')),
                ('scale_weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.scale_weight', verbose_name='Scale_weight')),
            ],
        ),
    ]