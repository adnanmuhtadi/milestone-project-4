# Generated by Django 3.2.4 on 2021-07-27 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contactus_cdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='ctime',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='cdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
