# Generated by Django 3.2.3 on 2022-12-24 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_consumerprofile_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producerprofile',
            old_name='company_email',
            new_name='store_email',
        ),
        migrations.RenameField(
            model_name='producerprofile',
            old_name='company_logo',
            new_name='store_logo',
        ),
        migrations.RenameField(
            model_name='producerprofile',
            old_name='company_name',
            new_name='store_name',
        ),
        migrations.RemoveField(
            model_name='consumerprofile',
            name='age',
        ),
        migrations.AddField(
            model_name='producerprofile',
            name='business_certificate',
            field=models.FileField(default=None, upload_to='Files'),
        ),
        migrations.AddField(
            model_name='producerprofile',
            name='location',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
