# Generated by Django 4.1 on 2024-02-28 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GuestApp', '0001_initial'),
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_application',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('child_name', models.CharField(max_length=100)),
                ('child_age', models.IntegerField()),
                ('child_gender', models.CharField(max_length=100)),
                ('child_image', models.ImageField(upload_to='')),
                ('child_healthdetails', models.CharField(max_length=500)),
                ('application_status', models.CharField(max_length=20)),
                ('application_no', models.BigIntegerField()),
                ('daycare_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.tbl_daycare')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GuestApp.tbl_parent')),
            ],
        ),
    ]
