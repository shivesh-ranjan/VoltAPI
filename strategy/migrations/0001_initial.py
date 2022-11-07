# Generated by Django 4.1.2 on 2022-10-29 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrategyModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.TextField()),
                ('problemArea', models.TextField()),
                ('uses', models.TextField()),
                ('startup', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.startup')),
            ],
            options={
                'ordering': ['startup'],
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategyModule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='strategies', to='strategy.strategymodule')),
                ('strategyTitle', models.CharField(max_length=255)),
                ('strategy', models.TextField()),
                ('category', models.CharField(choices=[('M', 'Major'), ('m', 'Minor')], default='M', max_length=1)),
                ('approxStartDate', models.DateField()),
                ('Customer', models.TextField()),
                ('features', models.TextField()),
                ('description', models.TextField()),
                ('success', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1)),
                ('strategyLeader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.profile')),
            ],
        ),
    ]
