# Generated by Django 4.0.6 on 2022-08-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_post2_id_alter_post2_page_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='post3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2000)),
                ('page_url', models.CharField(max_length=2000, unique=True)),
                ('picture_url', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=2000)),
                ('company', models.CharField(max_length=2000)),
                ('work', models.CharField(max_length=2000)),
                ('qualification', models.CharField(max_length=2000)),
                ('favor', models.CharField(max_length=2000)),
                ('welfare', models.CharField(max_length=2000)),
                ('skill_stack', models.CharField(max_length=2000)),
                ('place', models.CharField(max_length=2000)),
                ('money', models.CharField(max_length=2000)),
                ('employee', models.CharField(max_length=2000)),
                ('first_cleaned_welfare', models.CharField(max_length=2000)),
                ('first_cleaned_works', models.CharField(max_length=2000)),
                ('scaler_money', models.CharField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='post2',
        ),
    ]