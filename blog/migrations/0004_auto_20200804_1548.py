# Generated by Django 2.1.9 on 2020-08-04 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_company_category_nip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nip',
            old_name='Company',
            new_name='Company_ID',
        ),
    ]
