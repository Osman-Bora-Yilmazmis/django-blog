# Generated by Django 4.2 on 2023-04-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_yorummodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('isim_soyisim', models.CharField(max_length=150)),
                ('mesaj', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'iletisim',
                'verbose_name_plural': 'iletisim',
                'db_table': 'iletisim',
            },
        ),
    ]
