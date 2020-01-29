# Generated by Django 3.0.2 on 2020-01-27 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('duration', models.CharField(default='Forever', max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Employee')),
            ],
        ),
    ]