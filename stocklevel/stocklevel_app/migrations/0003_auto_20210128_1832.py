# Generated by Django 3.1.5 on 2021-01-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocklevel_app', '0002_auto_20210127_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='stock_level',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nazwa materiału wyjściowego'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='comment',
            field=models.TextField(null=True, verbose_name='Uwagi'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='component',
            field=models.ManyToManyField(to='stocklevel_app.Component', verbose_name='Materiał wyjściowy dostarczany przez dostawcę'),
        ),
        migrations.AlterField(
            model_name='warehouseentry',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocklevel_app.component', verbose_name='Nazwa materiału wyjściowego'),
        ),
        migrations.AlterField(
            model_name='warehouseentry',
            name='laboratory_series_number',
            field=models.CharField(help_text='Pole do uzupełnienia po wykonaniu badań wewnętrznych', max_length=100, null=True, verbose_name='Numer serii po badaniu'),
        ),
        migrations.AlterField(
            model_name='warehouseentry',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocklevel_app.supplier', verbose_name='Dostawca materiału'),
        ),
    ]
