# Generated by Django 2.2.6 on 2019-11-04 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='films.Film'),
        ),
    ]