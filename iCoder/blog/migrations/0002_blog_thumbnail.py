# Generated by Django 4.0.2 on 2022-02-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='blogs/uploads'),
            preserve_default=False,
        ),
    ]
