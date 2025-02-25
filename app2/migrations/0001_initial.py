# Generated by Django 5.1.4 on 2025-01-23 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('price', models.BigIntegerField()),
                ('discription', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='file')),
            ],
        ),
        migrations.CreateModel(
            name='order_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('gtotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=20)),
                ('phon', models.BigIntegerField()),
                ('addr', models.TextField()),
                ('loc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='order_child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.addproduct')),
                ('oid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.order_master')),
            ],
        ),
        migrations.AddField(
            model_name='order_master',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.reg'),
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('pword', models.CharField(max_length=20)),
                ('utype', models.CharField(max_length=20)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.reg')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField(default=1)),
                ('date', models.DateField(default='2000-02-02')),
                ('pid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app2.addproduct')),
                ('uid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app2.reg')),
            ],
        ),
    ]
