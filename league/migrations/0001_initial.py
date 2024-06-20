# Generated by Django 5.0.6 on 2024-06-20 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='league_logos/')),
                ('description', models.TextField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leagues', to=settings.AUTH_USER_MODEL)),
                ('teams', models.ManyToManyField(blank=True, related_name='league', to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('token', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('accepted', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='team.team')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='league.league')),
            ],
        ),
    ]
