# Generated by Django 3.2.4 on 2021-06-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0006_auto_20210621_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('profile_pics', models.ImageField(blank=True, upload_to='Profies')),
            ],
        ),
        migrations.DeleteModel(
            name='userProfile',
        ),
    ]
