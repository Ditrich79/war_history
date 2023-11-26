from django.db import models


class ArticleCategory(models.Model):
    category = models.CharField(max_length=150, unique=True, verbose_name="Категория")
    description = models.TextField(blank=True, verbose_name="Описание категории")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название статьи")
    description = models.TextField(blank=True, null=True, verbose_name="Содержание статьи")
    image = models.ImageField(upload_to="articles_images/", blank=True, verbose_name="Изображение")
    category = models.ForeignKey("ArticleCategory", on_delete=models.CASCADE, verbose_name="Категория")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статью"
        verbose_name_plural = "Статьи"
        ordering = ["-title"]


class Picture(models.Model):
    picture = models.ImageField(upload_to="articles_images/%Y/%m/%d/", blank=True, verbose_name="Картина")
    article = models.ForeignKey("Article", on_delete=models.CASCADE, blank=True, verbose_name="Статья")

    class Meta:
        verbose_name = "картину"
        verbose_name_plural = "Картины"
