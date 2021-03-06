# Generated by Django 3.2.7 on 2021-09-17 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_courseregister_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aboutteacher', verbose_name="O'qtuvchi"),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Telefon raqam'),
        ),
        migrations.AlterField(
            model_name='trainingregister',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Telefon raqam'),
        ),
    ]
