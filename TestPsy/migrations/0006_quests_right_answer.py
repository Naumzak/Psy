# Generated by Django 4.1.3 on 2022-11-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPsy', '0005_quests_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='quests',
            name='right_answer',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]