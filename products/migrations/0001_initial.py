# Generated by Django 4.2.1 on 2023-05-16 08:58

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', ckeditor.fields.RichTextField()),
                ('shor_description', ckeditor.fields.RichTextField(blank=True)),
                ('sizes', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
                ('color', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('datetime_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('datetime_edit', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]