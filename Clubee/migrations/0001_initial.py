# Generated by Django 2.0.9 on 2018-11-06 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('logo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MiembroClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clubee.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='miembroclub',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clubee.Usuario'),
        ),
        migrations.AddField(
            model_name='club',
            name='usuarios',
            field=models.ManyToManyField(through='Clubee.MiembroClub', to='Clubee.Usuario'),
        ),
    ]
