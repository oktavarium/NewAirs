from django.db import models
from django.utils import timezone


class Review(models.Model):
    user_name = models.CharField(max_length = 100, verbose_name="Имя")
    user_town = models.CharField(max_length = 100, verbose_name="Город")
    user_text = models.TextField(default="", verbose_name="Текст отзыва")
    answer_text = models.TextField(default="", verbose_name="Текст ответа на отзыв", blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата написания")
    confirmed = models.BooleanField(default=False, verbose_name="Подтверждено")

    class Meta():
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def publish(self):
        self.save()

    def get_text_preview(self):
        return self.user_text[:500]

    def __str__(self):
        return self.user_name


class AboutMe(models.Model):
    user_name = models.CharField(max_length = 100, verbose_name="Имя")
    user_mail = models.CharField(max_length = 100, verbose_name="Почта")
    user_phone = models.CharField(max_length=100, verbose_name="Телефон")
    user_insta = models.CharField(max_length=100, verbose_name="Инстаграм")
    user_skype = models.CharField(max_length=100, verbose_name="Скайп")
    user_periskop = models.CharField(max_length=100, verbose_name="Перископ")
    user_vk = models.CharField(max_length=100, verbose_name="ВК")
    user_fb = models.CharField(max_length=100, verbose_name="FB")
    user_tw = models.CharField(max_length=100, verbose_name="Twitter")
    user_copyright = models.TextField(default="", verbose_name="Копирайт")
    about_text = models.TextField(default="", verbose_name="Общее описание обо мне")
    about_short_text = models.TextField(default="", verbose_name="Короткое описание обо мне")

    class Meta():
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"

    def publish(self):
        self.save()

    def __str__(self):
        return self.user_name


class Story(models.Model):
    story_year = models.DateField(default=timezone.now, verbose_name="Дата события")
    story_text = models.CharField(max_length = 100, verbose_name="Описание")

    class Meta():
        verbose_name = "События из жизни"
        verbose_name_plural = "События из жизни"

    def publish(self):
        self.save()


class News(models.Model):
    news_name = models.CharField(max_length = 100, verbose_name="Название новости")
    news_date = models.DateTimeField(default=timezone.now, verbose_name="Дата новости")
    news_text = models.TextField(default="", verbose_name="Текст новости")
    news_image = models.ImageField(upload_to="media", verbose_name="Изображение", null=True)

    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def publish(self):
        self.save()

    def get_news_preview(self):
        return self.news_text[:500]


