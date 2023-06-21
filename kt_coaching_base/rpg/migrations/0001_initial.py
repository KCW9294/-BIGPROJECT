# Generated by Django 4.2 on 2023-06-21 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=45)),
                ('rank', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=4)),
                ('voice', models.CharField(max_length=45)),
                ('career', models.IntegerField()),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='nickname')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('voice_url', models.TextField()),
                ('csv_url', models.TextField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpg.persona')),
            ],
            options={
                'ordering': ('send_date',),
            },
        ),
    ]
