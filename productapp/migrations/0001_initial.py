# Generated by Django 4.2 on 2023-05-25 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catogary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catogary_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('catogary_offer', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('price', models.IntegerField(null=True)),
                ('stock', models.IntegerField(null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('product_offer', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('product_status', models.BooleanField(default=True)),
                ('Catogary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.catogary')),
            ],
        ),
    ]
