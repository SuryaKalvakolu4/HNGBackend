from django.db import models


class DailyPrize(models.Model):
    logo = models.ImageField()
    company_name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    prize_name = models.CharField(max_length=100)
    description = models.TextField()
    video_link = models.URLField()
    ig_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    yt_link = models.URLField(blank=True, null=True, verbose_name="Youtube link")

    class Meta:
        verbose_name = "Daily Prize"
        verbose_name_plural = "Daily Prizes"

    def __str__(self) -> str:
        return self.company_name


class Medal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name = "Medal"
        verbose_name_plural = "Medals"

    def __str__(self) -> str:
        return self.name


class Badge(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name = "Badge"
        verbose_name_plural = "Badges"

    def __str__(self) -> str:
        return self.name
