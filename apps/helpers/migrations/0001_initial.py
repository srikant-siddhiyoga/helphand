# Generated by Django 5.1 on 2024-08-28 11:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelperTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Helpers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('cost', models.FloatField()),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('zipcode', models.CharField(max_length=6)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('helper_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpers.helpertypes')),
            ],
        ),
    ]
