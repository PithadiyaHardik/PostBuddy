# Generated by Django 3.2.4 on 2021-06-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_friends2_friends_friends2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='owner_id',
        ),
        migrations.AddField(
            model_name='posts',
            name='owner_username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]