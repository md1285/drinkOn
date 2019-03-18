# Generated by Django 2.1.5 on 2019-03-18 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_auto_20190318_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HoursVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Hours')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_photo_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MenuVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_assigned_id', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Restaurant'),
        ),
        migrations.AddField(
            model_name='hours',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Restaurant'),
        ),
    ]
