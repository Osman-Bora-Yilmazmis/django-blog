# Generated by Django 4.2 on 2023-04-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_iletisimmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yazilarmodel',
            old_name='duzenleme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
        migrations.RenameField(
            model_name='yazilarmodel',
            old_name='oluşturulma_tarihi',
            new_name='olusturulma_tarihi',
        ),
        migrations.RenameField(
            model_name='yorummodel',
            old_name='guncellenme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
    ]
