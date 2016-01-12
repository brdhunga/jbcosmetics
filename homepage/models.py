from django.db import models


class HomePageBanner(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    background_image = models.ImageField(upload_to='homepage_banners/%Y/%m/%d', blank=True)
    url = models.URLField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.title