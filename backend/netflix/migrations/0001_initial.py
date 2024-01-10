# Generated by Django 5.0 on 2024-01-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('cast', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('release_year', models.PositiveSmallIntegerField()),
                ('rating', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('director', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(default='TV show', max_length=10)),
                ('director', models.CharField(default='None', max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('rating', models.CharField(max_length=15)),
                ('duration', models.CharField(max_length=15)),
                ('release_year', models.PositiveSmallIntegerField()),
                ('catalog', models.CharField(max_length=15)),
                ('average_score', models.FloatField(null=True)),
                ('score_count', models.IntegerField(null=True)),
                ('comments', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('catalog', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=30)),
                ('duration', models.CharField(default='0', max_length=15)),
            ],
        ),
    ]
