# Generated by Django 5.0 on 2024-01-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0005_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='cast',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cast',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='country',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='rating',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='data',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='director',
            name='director',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='director',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='form',
            name='cast',
            field=models.CharField(default='NAME', max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='catalog',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='form',
            name='country',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='director',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='form',
            name='duration',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='form',
            name='rating',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='form',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='form',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='form',
            name='type',
            field=models.CharField(default='TV show', max_length=100),
        ),
        migrations.AlterField(
            model_name='listed',
            name='catalog',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='listed',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='director',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='duration',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='type',
            field=models.CharField(choices=[('TV Show', 'TV Show'), ('Movie', 'Movie')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='show_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
