# Generated by Django 2.1.4 on 2018-12-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0010_auto_20181226_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='medimage',
            name='emr_file',
            field=models.FileField(blank=True, upload_to='', verbose_name='EMR File'),
        ),
        migrations.AddField(
            model_name='medimage',
            name='pacs_file',
            field=models.FileField(blank=True, upload_to='', verbose_name='PACS File'),
        ),
    ]