# Generated by Django 3.0.7 on 2020-09-22 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('project', models.CharField(max_length=30, verbose_name='项目名称')),
                ('reporter', models.CharField(max_length=10, verbose_name='周报填写人')),
                ('this_report', models.TextField(max_length=300, verbose_name='本周周报')),
                ('last_report', models.TextField(max_length=300, verbose_name='上周周报')),
                ('last_complete', models.CharField(max_length=10, verbose_name='上周完成情况')),
                ('last_reson', models.CharField(max_length=225, verbose_name='上周未完成原因')),
                ('need_help', models.CharField(max_length=255, verbose_name='需要公司协调的事项')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='周报创建时间')),
                ('week_number', models.CharField(max_length=10, verbose_name='周数')),
            ],
            options={
                'db_table': 'report',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
