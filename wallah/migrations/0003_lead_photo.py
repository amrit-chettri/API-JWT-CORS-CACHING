# Generated by Django 5.0 on 2024-10-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallah', '0002_delete_orders_delete_products_remove_lead_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='test/images'),
        ),
    ]