# Generated by Django 3.2 on 2021-04-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conference', '0002_auto_20210430_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cityy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='City',
            field=models.CharField(max_length=600),
        ),
    ]
