# Generated by Django 2.0.3 on 2018-03-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_heading',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_text',
            field=models.CharField(max_length=700),
        ),
    ]