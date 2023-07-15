# Generated by Django 4.2 on 2023-07-12 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productapp', '0003_rename_catogary_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('guest_user', models.CharField(blank=True, max_length=200, null=True)),
                ('cancel_status', models.BooleanField(blank=True, default=False, null=True)),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]