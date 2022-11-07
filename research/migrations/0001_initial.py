# Generated by Django 4.1.2 on 2022-10-29 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('strategy', '0001_initial'),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionalArticles', models.TextField(blank=True, null=True)),
                ('startup', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.startup')),
            ],
            options={
                'ordering': ['startup'],
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('researchTitle', models.TextField()),
                ('category', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary')], default='P', max_length=1)),
                ('researchTask', models.TextField()),
                ('conclusion', models.TextField()),
                ('researchArtifacts', models.TextField(blank=True, null=True)),
                ('researchLeader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.profile')),
                ('researchModule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='researches', to='research.researchmodule')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.strategy')),
            ],
        ),
    ]
