# Generated by Django 3.0 on 2022-12-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('utype', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('rank', models.IntegerField()),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=7)),
                ('price_btc', models.DecimalField(decimal_places=7, max_digits=8)),
                ('volume_usd_24h', models.DecimalField(decimal_places=2, max_digits=14)),
                ('market_cap_usd', models.DecimalField(decimal_places=2, max_digits=14)),
                ('available_supply', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_supply', models.DecimalField(decimal_places=2, max_digits=20)),
                ('max_supply', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('percent_change_1h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percent_change_24h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percent_change_7d', models.DecimalField(decimal_places=2, max_digits=5)),
                ('last_updated', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Cryptocurrency',
                'verbose_name_plural': 'Cryptocurrencies',
            },
        ),
    ]
