# Generated by Django 3.2.6 on 2021-08-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0003_auto_20210830_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='nota',
            new_name='nota1',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='nota',
        ),
        migrations.AddField(
            model_name='curso',
            name='nota1',
            field=models.IntegerField(default=12, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='nota2',
            field=models.IntegerField(default=12, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='nota3',
            field=models.IntegerField(default=12, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='nota4',
            field=models.IntegerField(default=12, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='nota5',
            field=models.IntegerField(default=12, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='nota2',
            field=models.IntegerField(default=14, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='nota3',
            field=models.IntegerField(default=15, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='nota4',
            field=models.IntegerField(default=16, verbose_name=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='nota5',
            field=models.IntegerField(default=17, verbose_name=2),
            preserve_default=False,
        ),
    ]
