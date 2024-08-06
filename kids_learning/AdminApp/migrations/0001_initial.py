# Generated by Django 4.1 on 2024-02-28 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('categoryid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=50)),
                ('categoryimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_district',
            fields=[
                ('districtid', models.AutoField(primary_key=True, serialize=False)),
                ('districtname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_subcategory',
            fields=[
                ('subcategoryid', models.AutoField(primary_key=True, serialize=False)),
                ('subcategoryname', models.CharField(max_length=50)),
                ('subcategoryimage', models.ImageField(upload_to='')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.tbl_category')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_location',
            fields=[
                ('locationid', models.AutoField(primary_key=True, serialize=False)),
                ('locationname', models.CharField(max_length=50)),
                ('districtid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.tbl_district')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_daycare',
            fields=[
                ('daycare_id', models.AutoField(primary_key=True, serialize=False)),
                ('daycare_landmark', models.CharField(max_length=50)),
                ('daycare_pincode', models.IntegerField()),
                ('branch_name', models.CharField(max_length=50)),
                ('daycare_image', models.ImageField(upload_to='')),
                ('daycare_contact', models.BigIntegerField()),
                ('description', models.CharField(max_length=50, null=True)),
                ('daycare_email', models.CharField(max_length=50)),
                ('daycare_map', models.CharField(max_length=50)),
                ('application_fee', models.FloatField(null=True)),
                ('monthly_fee', models.FloatField(null=True)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.tbl_location')),
            ],
        ),
    ]
