# Generated by Django 4.0 on 2021-12-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='return_devolucao',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
