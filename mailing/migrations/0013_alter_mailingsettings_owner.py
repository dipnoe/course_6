# Generated by Django 4.2.4 on 2023-08-20 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0012_alter_mailingsettings_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец рассылки'),
        ),
    ]