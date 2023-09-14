# Generated by Django 4.2.5 on 2023-09-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(choices=[(1, 'ativo'), (2, 'inativo')], default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        ),
    ]
