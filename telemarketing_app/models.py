from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
import re 
from datetime import datetime

def validate_phone_number(phone_number):
    reg_pattern = re.compile(r"(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$")
    if not reg_pattern.match(phone_number):
        raise ValidationError(
            gettext_lazy('%(phone_number)s некорректный номер'),
            params={'phone_number': phone_number}
        )

class Account(models.Model):
    class Meta:
        db_table="accounts"
        verbose_name="Аккаунты"
        verbose_name_plural="Аккаунты"

    id_doc=models.IntegerField(primary_key=True, verbose_name="ID аккаунта")
    doc_name=models.TextField(verbose_name="Ограничения")
    doc_type=models.TextField(verbose_name="Пакет услуг")
    doc_date=models.DateField(verbose_name="Дата создания аккаунта")

    def __str__(self) -> str:  
        return f'''{self.id_doc} {self.doc_name} {self.doc_type} {self.doc_date}'''
        
class Client(models.Model):
    class Meta:
        db_table = "client"
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"

    Genders = (
        ('M', 'Мужской'),
        ('F', 'Женский')
    )

    id_client = models.IntegerField(primary_key=True, verbose_name="ID клиента")
    first_name = models.TextField(verbose_name="Имя")
    last_name = models.TextField(verbose_name="Фамилия")
    patronymic = models.TextField(verbose_name="Отчество", blank=True, null=True)
    date_birth = models.DateField(verbose_name="Дата рождения")
    id_passport = models.IntegerField(verbose_name="Номер и серия паспорта", blank=True, null=True)
    gender = models.CharField(verbose_name="Пол", choices=Genders, max_length=1) 
    phone_number = models.TextField(verbose_name="Номер телефона", validators=[validate_phone_number])
    id_account = models.ForeignKey(Account, on_delete=models.RESTRICT, verbose_name='ID аккаунта', blank=True, null=True)

    def __str__(self) -> str:  
        return f'''{self.id_client} {self.first_name} {self.last_name} {self.patronymic} {self.date_birth} {self.id_passport}
        {self.gender} {self.phone_number}'''
        
class Employee(models.Model):
    class Meta:
        db_table = "employee"
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"

    Genders = (
        ('M', 'Мужской'),
        ('F', 'Женский')
    )

    id_employee = models.IntegerField(primary_key=True, verbose_name="ID сотрудника")
    first_name = models.TextField(verbose_name="Имя")
    last_name = models.TextField(verbose_name="Фамилия")
    patronymic = models.TextField(verbose_name="Отчество", blank=True, null=True)
    date_birth = models.DateField(verbose_name="Дата рождения")
    id_passport = models.IntegerField(verbose_name="Номер и серия паспорта", blank=True, null=True)
    gender = models.CharField(verbose_name="Пол", choices=Genders, max_length=1) 
    phone_number = models.TextField(verbose_name="Номер телефона", validators=[validate_phone_number])
    date_employment = models.DateField(verbose_name="Дата принятия на работу")
    date_dismissal = models.DateField(verbose_name="Дата увольнения", blank=True, null=True)
    id_work = models.ForeignKey(Account, on_delete=models.RESTRICT, verbose_name='ID встречи', blank=True, null=True)

    def __str__(self) -> str:  
        return f'''{self.id_employee} '''

def status_validator(work_status):
    if work_status not in ["Успешно", "Неуспешно"]:
        raise ValidationError(
            gettext_lazy('%(work_status)s is wrong work status'),
            params={'work_status': work_status},
        )

class Work(models.Model):
    class Meta:
        db_table="work"
        verbose_name="Встречи"
        verbose_name_plural="Встречи"

    id_work=models.IntegerField(primary_key=True, verbose_name="ID встречи")
    work_status=models.CharField(verbose_name="Результат встречи\n(Успешно, Неуспешно)",validators=[status_validator])
    id_employee=models.ForeignKey(Employee, verbose_name="ID Сотрудника",on_delete=models.RESTRICT)

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)