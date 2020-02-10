# Generated by Django 3.0.1 on 2020-02-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200205_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Number', models.FloatField()),
                ('Checkin', models.DateField()),
                ('Checkout', models.DateField()),
                ('Noofpeople', models.IntegerField()),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
