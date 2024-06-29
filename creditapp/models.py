from django.db import models
from django.urls import reverse
# Create your models here.

STATUS = (
    ('active', "Active"),
    ('deactive', "Deactive"),
)






class MainCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')

    status = models.BooleanField(default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'M.Kategoriya'
        verbose_name_plural = "M.Kategoriyalar"
        ordering = ('-created_at',)

    
    def __str__(self):
        return self.name
    

    # def get_absolute_url(self):
    #     return reverse('arti')






class Category(models.Model):
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='category_main', verbose_name="Kategoriya nomi")
    info = models.TextField()
    news = models.CharField(max_length=250, verbose_name='Yangiliklar')

    status = models.BooleanField(default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = "Kategoriyalar"
        ordering = ('-created_at',)

    
    def __str__(self):
        return self.news
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



class Comment(models.Model):
    # # # # post = models.ForeignKey(Transfers, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    body = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')

    class Meta:
        verbose_name = "Komentariya"
        verbose_name_plural = "Komentariyalar"
        ordering = ("-created_at",)

    def str(self):
        text = f"{self.name}  - {self.email}"
        return text






class Co_workers(models.Model):
    name = models.CharField(max_length=75, verbose_name='Hamkorlar')
    comission = models.PositiveIntegerField(default=10, verbose_name='Komissiya')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = "Hamkorlar"
        ordering = ('-created_at', )


    def __str__(self) -> str:
        return self.name






class Products(models.Model):
    plastic_cards = models.TextField(verbose_name='Plastik Karta')
    credit_cards = models.TextField(verbose_name='Kredit Karta')
    contribution = models.TextField(verbose_name='Hissa')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Tovar'
        verbose_name_plural = "Tovarlar"
        ordering = ('-created_at', )


    def __str__(self) -> str:
        return self.plastic_cards
    



class Transfers(models.Model):
    co_workers = models.ForeignKey(Co_workers, on_delete=models.CASCADE, related_name='transfer_workers')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='transfer_comment')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Perevod'
        verbose_name_plural = "Perevodlar"
        ordering = ('-created_at', )





class Tariffs(models.Model):
    info = models.CharField(max_length=175, verbose_name='Informatsiya')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='tariff_comment')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Tarif'
        verbose_name_plural = "Tariflar"
        ordering = ('-created_at', )


    def __str__(self) -> str:
        return self.info
    



class Job_Openings(models.Model):
    about = models.TextField(verbose_name='Kategoriya Xaqida')
    openings = models.CharField(max_length=50, verbose_name='Vakansiya')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='openings_comment')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = "Vakansiyalar"
        ordering = ('-created_at', )


    def __str__(self) -> str:
        return self.openings





class Tender(models.Model):
    tender = models.CharField(max_length=75, verbose_name='Tender')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='tender_comment')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Tender'
        verbose_name_plural = "Tenderlar"
        ordering = ('-created_at', )


    def __str__(self) -> str:
        return self.tender




class Individuals(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, related_name='tender_individual')
    co_workers = models.ForeignKey(Co_workers, on_delete=models.CASCADE, related_name='worker_individual')
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_individual')
    transfers = models.ForeignKey(Transfers, on_delete=models.CASCADE, related_name='transfer_individual')
    tariffs = models.ForeignKey(Tariffs, on_delete=models.CASCADE, related_name='tariff_individual')
    job_Openings = models.ForeignKey(Job_Openings, on_delete=models.CASCADE, related_name='opening_individual')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='individual_comment')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Fiz. Li.'
        verbose_name_plural = "Fiz. Li."
        ordering = ('-created_at', )



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Joining(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')

    class Meta:
        verbose_name = "Qo'shilish"
        verbose_name_plural = "Qo'shilishlar"
        ordering = ("-created_at",)

    def str(self):
        text = f"{self.full_name}  - {self.email}"
        return text




class About_Us(models.Model):
    information = models.CharField(max_length=150, verbose_name='Informatsiya')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Biz'
        verbose_name_plural = "Bizlar"
        ordering = ('-created_at', )


    def __str__(self):
        return self.information



class Be_Co_Worker(models.Model):
    joining = models.ForeignKey(Joining, on_delete=models.CASCADE, related_name='join_worker')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Hohlash'
        verbose_name_plural = "Hohlashlar"
        ordering = ('-created_at', )



class LegalEntities(models.Model):
    about_us = models.ForeignKey(About_Us, on_delete=models.CASCADE, related_name='about_entities')
    be_co_worker = models.ForeignKey(Be_Co_Worker, on_delete=models.CASCADE, related_name='worker_entities')
    joining = models.ForeignKey(Joining, on_delete=models.CASCADE, related_name='join_entities')

    status = models.CharField(max_length=20, choices=STATUS, default=True, verbose_name='Holati')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Yurid. Li.'
        verbose_name_plural = "Yurid. Li."
        ordering = ('-created_at', )


