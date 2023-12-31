# Generated by Django 4.2.6 on 2023-12-12 08:37

from django.db import migrations, models
import telemarketing_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('telemarketing_app', '0002_remove_documents_patronymic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(verbose_name='Наименование подразделения'),
        ),
        migrations.AlterField(
            model_name='trud',
            name='order_status',
            field=models.CharField(validators=[telemarketing_app.models.status_validator], verbose_name='Статус заявки\n(Открыта, Закрыта, На рассмотрении)'),
        ),
    ]
