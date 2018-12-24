# Generated by Django 2.1.4 on 2018-12-24 17:52

from django.db import migrations, models
import mapping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0007_auto_20181224_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medimage',
            name='dicom_jpg_file',
            field=mapping.fields.ThumbnailImageField(blank=True, upload_to='medimage/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='medimage',
            name='pacs_file',
            field=models.FileField(blank=True, upload_to='', verbose_name='PACS File'),
        ),
    ]