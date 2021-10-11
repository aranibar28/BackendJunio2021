# Generated by Django 3.2.7 on 2021-09-12 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('modelo', models.CharField(choices=[('deportivo', 'Deportivo'), ('Hatchback', 'Hatchback'), ('suv', 'Suv'), ('sedan', 'Sedan')], max_length=10)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.auto')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('marca', models.CharField(choices=[('bmw', 'Bmw'), ('citroen', 'Citroen'), ('ferrari', 'Ferrari'), ('ford', 'Ford'), ('mercedes', 'Mercedes'), ('porsche', 'Porsche'), ('renault', 'Renault'), ('tesla', 'Tesla'), ('toyota', 'Toyota'), ('Volkswagen', 'Volkswagen')], max_length=10)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.auto')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
    ]
