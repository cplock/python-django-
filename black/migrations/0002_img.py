# Generated by Django 2.1.1 on 2019-05-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img', verbose_name='资源图片')),
                ('img_name', models.CharField(max_length=20, verbose_name='图片名')),
                ('wpurl', models.CharField(max_length=200, verbose_name='图片标识网盘地址')),
            ],
            options={
                'verbose_name': '资源图片',
                'verbose_name_plural': '资源图片',
                'db_table': 'Img_source',
            },
        ),
    ]