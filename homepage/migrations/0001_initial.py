# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=200, blank=True)),
                ('background_image', models.ImageField(upload_to=b'homepage_banners/%Y/%m/%d', blank=True)),
                ('url', models.URLField(default=b'', blank=True)),
            ],
        ),
    ]
