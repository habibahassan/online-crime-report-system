# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-01 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseClose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dateofregister', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseStatus',
            fields=[
                ('casenumber', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('courtname', models.CharField(max_length=200)),
                ('dateofregister', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaintid', models.AutoField(primary_key=True, serialize=False)),
                ('dateofcomplaint', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('policestation', models.CharField(max_length=120)),
                ('location', models.TextField()),
                ('user', models.CharField(default='Annonymous', max_length=120)),
                ('status', models.CharField(choices=[('Complaint Registered', 'Complaint Registered'), ('FIR Filed', 'FIR Filed'), ('Case Open', 'Case Open'), ('Case Closed', 'Case Closed')], default='Complaint Registered', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CopStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dateofregister', models.DateTimeField(auto_now_add=True)),
                ('complaintid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='Fir',
            fields=[
                ('firid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('signedby', models.CharField(max_length=20)),
                ('content', models.TextField(default='First Information Report not yet submitted')),
                ('complaintid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.Complaint')),
            ],
        ),
        migrations.AddField(
            model_name='casestatus',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.Complaint'),
        ),
        migrations.AddField(
            model_name='caseclose',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.Complaint'),
        ),
    ]