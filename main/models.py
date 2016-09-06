from django.db import models
from django.utils import timezone


class Review(models.Model):
    user_name = models.CharField(max_length=100, verbose_name="Имя")
    user_town = models.CharField(max_length=100, verbose_name="Город")
    user_text = models.TextField(max_length=500, default="", verbose_name="Текст отзыва")
    answer_text = models.TextField(default="", verbose_name="Текст ответа на отзыв", blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата написания")
    confirmed = models.BooleanField(default=False, verbose_name="Подтверждено")
    to_main = models.BooleanField(default=False, verbose_name="на главную страницу")

    class Meta():
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def publish(self):
        self.save()

    def get_text_preview(self):
        return self.user_text[:500]

    def __str__(self):
        return self.user_name


class Email(models.Model):
    user_name = models.CharField(max_length=100, verbose_name="Имя")
    user_email = models.EmailField(max_length=100, verbose_name="Email")
    user_text = models.TextField(max_length=500, default="", verbose_name="Текст")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата написания")

    class Meta():
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"

    def publish(self):
        self.save()

    def __str__(self):
        return self.user_name


class AboutMe(models.Model):
    data_fields = (
        ("name", "Имя"),
        ("email", "Email"),
        ("phone", "Телефон"),
        ("instagram", "Instagram"),
        ("skype", "Skype"),
        ("periskop", "Periskop"),
        ("vk", "Vk"),
        ("fb", "Fb"),
        ("copyright", "Copyright"),
        ("twitter", "Twitter"),
        ("about_me", "Обо мне"),
        ("about_me_short", "Обо мне коротко"),
    )
    user_field = models.CharField(max_length=30, primary_key=True,default="name",
                                  verbose_name="Выберите раздел", choices=data_fields)
    user_data = models.CharField(max_length=1000, verbose_name="Данные", default="")

    class Meta():
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"

    def publish(self):
        self.save()

    def __str__(self):
        return self.user_field


class Story(models.Model):
    story_year = models.DateField(default=timezone.now, verbose_name="Дата события")
    story_text = models.CharField(max_length=100, verbose_name="Описание")

    class Meta():
        verbose_name = "События из жизни"
        verbose_name_plural = "События из жизни"

    def publish(self):
        self.save()


class News(models.Model):
    news_name = models.CharField(max_length=100, verbose_name="Название новости")
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


