# Generated by Django 3.0.7 on 2020-08-23 10:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enquaryformappp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquarydata',
            name='trainers',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mani', 'mani'), ('chinna', 'chinna'), ('chitti', 'chitti')], max_length=200),
        ),
    ]
