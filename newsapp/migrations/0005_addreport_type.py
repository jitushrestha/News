# Generated by Django 4.0 on 2022-03-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_addreport_approval_alter_addreport_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addreport',
            name='Type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
