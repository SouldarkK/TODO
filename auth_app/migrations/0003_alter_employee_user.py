# Generated by Django 4.0.2 on 2022-02-15 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
