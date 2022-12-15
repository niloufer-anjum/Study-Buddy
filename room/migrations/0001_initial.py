# Generated by Django 4.1.3 on 2022-12-14 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participant.participant')),
                ('participants', models.ManyToManyField(related_name='participant', to='participant.participant')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=500)),
                ('post', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participant.participant')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
    ]
