# Generated by Django 4.2.3 on 2023-07-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_admin_post_desc_alter_admin_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_post',
            name='desc',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='admin_post',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]