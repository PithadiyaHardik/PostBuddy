# Generated by Django 3.2.4 on 2021-06-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210621_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField()),
                ('privacy', models.CharField(max_length=10)),
                ('captions', models.TextField(blank=True)),
                ('post_image', models.ImageField(blank=True, upload_to='Posts')),
            ],
        ),
    ]
