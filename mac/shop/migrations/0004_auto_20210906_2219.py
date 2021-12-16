# Generated by Django 3.1.5 on 2021-09-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210825_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('cont_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=400)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=400),
        ),
    ]