# Generated by Django 4.1.13 on 2024-02-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=15, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
                ('tag_id', models.CharField(max_length=30, unique=True)),
                ('amount_saved', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_available', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trust_score_token', models.CharField(max_length=10)),
                ('user_type', models.CharField(choices=[('provider', 'Provider'), ('customer', 'Customer')], max_length=10)),
            ],
        ),
    ]
