from django.conf import settings
from django.db import models
from django.urls import reverse


class Clinic(models.Model):
    clinic_name = models.CharField(max_length=25)
    loca_goverment = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'clinic'
        verbose_name_plural = 'clinics'
    def __str__(self):
        return f'{self.clinic_name}'


class Children(models.Model):

    GENDER = (('MALE','Male'),('FEMALE','Female'),)
    registrar = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    clinic =  models.ForeignKey(Clinic, on_delete=models.CASCADE,related_name='children',)
    ward = models.CharField(max_length=14)
    card_number = models.CharField(max_length=10)
    firs_name = models.CharField(max_length=25)
    certificate_number = models.CharField(max_length=10)
    mother_name = models.CharField(max_length=25)
    father_name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    gender = models.CharField(max_length=6,choices=GENDER,default='GENDER')
    date_of_birth = models.DateField(auto_now_add=True)
    creates = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'child'
        verbose_name_plural = 'children'

    def __str__(self):
        return f'{self.firs_name}  {self.father_name}'

    def get_absolute_url(self):
        return reverse('child_detail', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('child_antegen', args=[str(self.id)])


class Antegen(models.Model):
    children =  models.ForeignKey(Children,on_delete=models.CASCADE,related_name='antegens',)
    date  = models.DateField()
    title = models.CharField(max_length=5)
    nex_coming = models.DateField()

    class Meta:
        verbose_name = 'antegen'
        verbose_name_plural = 'antegens'

    def __str__(self):
        return f' {self.children} received his {self.title} on {self.date} , his next coming is on {self.nex_coming}'
