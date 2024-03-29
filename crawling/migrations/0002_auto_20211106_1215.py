# Generated by Django 2.2.5 on 2021-11-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsdEuroRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='نسبت دلار به یورو')),
                ('time', models.DateTimeField(verbose_name='زمان')),
            ],
            options={
                'verbose_name': 'نسبت لحظه ای دلار به یورو',
                'verbose_name_plural': 'نسبت لحظه ای دلار به یورو',
            },
        ),
        migrations.AlterModelOptions(
            name='currentprice',
            options={'verbose_name': 'قیمت لحظه ای ارز', 'verbose_name_plural': 'قیمت لحظه ای ارز'},
        ),
        migrations.RemoveField(
            model_name='currentprice',
            name='euro',
        ),
        migrations.RemoveField(
            model_name='currentprice',
            name='ratio',
        ),
        migrations.RemoveField(
            model_name='currentprice',
            name='usd',
        ),
        migrations.AddField(
            model_name='currentprice',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AddField(
            model_name='currentprice',
            name='name',
            field=models.CharField(default='usd', max_length=20, verbose_name='نام'),
        ),
    ]
