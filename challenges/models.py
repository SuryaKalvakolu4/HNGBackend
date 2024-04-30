from django.db import models


LEVEL_CHOICE = (
    ("moderate", "moderate"),
    ("intense", "intense"),
)


class Challenge(models.Model):
    day = models.CharField(max_length=100, verbose_name="Challenge day", blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=100, blank=True, null=True)
    video_link = models.URLField(max_length=250, blank=True, null=True)
    moderate_physical = models.ForeignKey("ModeratePhysicalChallenge", on_delete=models.SET_NULL, blank=True, null=True)
    intense_physical = models.ForeignKey("IntensePhysicalChallenge", on_delete=models.SET_NULL, blank=True, null=True)
    mental = models.ForeignKey("MentalChallenge", on_delete=models.SET_NULL, blank=True, null=True)
    social = models.ForeignKey("SocialChallenge", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Challenge'
        verbose_name_plural = 'Challenges'

    def __str__(self) -> str:
        return self.day


class CommonChallengeFields(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    day = models.CharField(max_length=100, verbose_name="Challenge day", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class AbstractPhysicalChallenge(CommonChallengeFields):
    workout_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    required_equipments = models.CharField(max_length=100, blank=True, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, blank=True, null=True)
    video = models.URLField(max_length=250, blank=True, null=True)
    
    class Meta:
        abstract = True


class ModeratePhysicalChallenge(AbstractPhysicalChallenge):
    workout_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    required_equipments = models.CharField(max_length=100, blank=True, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, blank=True, null=True)
    video = models.URLField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Moderate Physical Challenge'
        verbose_name_plural = 'Moderate Physical Challenges'

    def __str__(self) -> str:
        return self.day


class IntensePhysicalChallenge(AbstractPhysicalChallenge):
    workout_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    required_equipments = models.CharField(max_length=100, blank=True, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, blank=True, null=True)
    video = models.URLField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Intense Physical Challenge'
        verbose_name_plural = 'Intense Physical Challenges'

    def __str__(self) -> str:
        return self.day


class SocialChallenge(CommonChallengeFields):
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Social Challenge'
        verbose_name_plural = 'Social Challenges'

    def __str__(self) -> str:
        return self.day


class MentalChallenge(CommonChallengeFields):
    voice_recording = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Mental Challenge'
        verbose_name_plural = 'Mental Challenges'

    def __str__(self) -> str:
        return self.day


class Instructor(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="Instructor name")
    description = models.TextField()
    ig_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    yt_link = models.URLField(blank=True, null=True, verbose_name="Youtube link")
    
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self) -> str:
        return self.name
