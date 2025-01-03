# Generated by Django 4.2.7 on 2024-12-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_certificate_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('preply', 'Preply Tutor'), ('freelance', 'Freelance Tutor'), ('other', 'Other')], default='other', max_length=20)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('details', models.JSONField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
