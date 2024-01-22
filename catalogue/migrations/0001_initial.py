# Generated by Django 4.2.1 on 2024-01-22 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sex', models.CharField(blank=True, max_length=32, null=True)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('character', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='animals_images')),
            ],
            options={
                'verbose_name': 'animal',
                'verbose_name_plural': 'animals',
            },
        ),
        migrations.CreateModel(
            name='AnimalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.animal')),
            ],
        ),
    ]