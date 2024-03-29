# Generated by Django 3.2.8 on 2021-12-01 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antegen',
            name='children',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='antegen', to='children.children'),
        ),
        migrations.AlterField(
            model_name='children',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='GENDER', max_length=6),
        ),
    ]
