# Generated by Django 4.0.3 on 2022-06-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_part', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dns_node_models',
            name='is_raw_regex_black',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dns_node_models',
            name='is_raw_regex_white_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dns_node_models',
            name='is_raw_white_list',
            field=models.BooleanField(default=False),
        ),
    ]
