# Generated by Django 4.0 on 2021-12-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookanestimate',
            options={'verbose_name_plural': 'Book An Estimate Inquiries'},
        ),
        migrations.AlterModelOptions(
            name='contactusinquiries',
            options={'verbose_name_plural': 'Contact Us Inquiries'},
        ),
        migrations.RemoveField(
            model_name='bookanestimate',
            name='service',
        ),
        migrations.AddField(
            model_name='bookanestimate',
            name='service',
            field=models.ManyToManyField(to='applications.Service'),
        ),
    ]
