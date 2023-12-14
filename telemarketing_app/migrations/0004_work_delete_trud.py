# Generated by Django 4.2.6 on 2023-12-12 14:00

from django.db import migrations, models
import django.db.models.deletion
import telemarketing_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('telemarketing_app', '0003_alter_department_department_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id_order', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID встречи')),
                ('order_status', models.CharField(validators=[telemarketing_app.models.status_validator], verbose_name='Результат встречи\n(Успешно, Неуспешно)')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='telemarketing_app.employee', verbose_name='ID Сотрудника')),
            ],
            options={
                'verbose_name': 'Встречи',
                'verbose_name_plural': 'Встречи',
                'db_table': 'work',
            },
        ),
        migrations.DeleteModel(
            name='Trud',
        ),
    ]
