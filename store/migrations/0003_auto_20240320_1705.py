# Generated by Django 5.0.3 on 2024-03-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_address_zip'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
            """, """
            DELETE FROM store_collection
            WHERE title='collection1'
            """)
    ]