# Generated by Django 2.0.7 on 2019-02-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.TextField(default='yes')),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
