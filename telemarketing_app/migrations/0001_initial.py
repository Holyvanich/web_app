# Generated by Django 4.2.6 on 2023-12-10 10:51

from django.db import migrations, models
import django.db.models.deletion
import telemarketing_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id_department', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID подразделения')),
                ('department_name', models.TextField(verbose_name='Наименование подразделения')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id_doc', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID документа')),
                ('doc_name', models.TextField(verbose_name='Наименование документа')),
                ('doc_type', models.TextField(verbose_name='Тип документа')),
                ('patronymic', models.TextField(verbose_name='Отчество')),
                ('doc_date', models.DateField(verbose_name='Дата создания документа')),
            ],
            options={
                'verbose_name': 'Документы',
                'verbose_name_plural': 'Документы',
                'db_table': 'documents',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id_employee', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID сотрудника')),
                ('first_name', models.TextField(verbose_name='Имя')),
                ('last_name', models.TextField(verbose_name='Фамилия')),
                ('patronymic', models.TextField(blank=True, null=True, verbose_name='Отчество')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('id_passport', models.IntegerField(blank=True, null=True, verbose_name='Номер и серия паспорта')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол')),
                ('phone_number', models.TextField(validators=[telemarketing_app.models.validate_phone_number], verbose_name='Номер телефона')),
                ('date_employment', models.DateField(verbose_name='Дата принятия на работу')),
                ('date_dismissal', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
                ('position', models.TextField(verbose_name='Должность')),
                ('id_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='telemarketing_app.department', verbose_name='Подразделение')),
                ('id_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='telemarketing_app.documents', verbose_name='ID документа')),
            ],
            options={
                'verbose_name': 'Сотрудники',
                'verbose_name_plural': 'Сотрудники',
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Trud',
            fields=[
                ('id_order', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID заявки')),
                ('order_status', models.TextField(validators=[telemarketing_app.models.status_validator], verbose_name='Статус заявки')),
                ('id_department', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='telemarketing_app.department', verbose_name='ID Подразделения')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='telemarketing_app.employee', verbose_name='ID Сотрудника')),
            ],
            options={
                'verbose_name': 'Трудоустройство',
                'verbose_name_plural': 'Трудоустройство',
                'db_table': 'trud',
            },
        ),
    ]
