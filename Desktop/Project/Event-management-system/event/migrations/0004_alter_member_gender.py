# Generated by Django 3.2.8 on 2021-12-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_rename_planname_plan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
