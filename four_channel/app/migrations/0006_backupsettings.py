# Generated by Django 5.1.6 on 2025-04-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_measurementdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backup_date', models.CharField(max_length=100)),
                ('confirm_backup', models.BooleanField(default=False)),
            ],
        ),
    ]
