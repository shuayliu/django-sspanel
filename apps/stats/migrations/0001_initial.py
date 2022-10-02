# Generated by Django 3.1.4 on 2021-01-09 12:36

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DailyStats",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(unique=True, verbose_name="创建日期"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "new_user_count",
                    models.BigIntegerField(default=0, verbose_name="新用户数量"),
                ),
                (
                    "active_user_count",
                    models.BigIntegerField(default=0, verbose_name="活跃户数量"),
                ),
                (
                    "checkin_user_count",
                    models.BigIntegerField(default=0, verbose_name="签到用户数量"),
                ),
                (
                    "order_count",
                    models.BigIntegerField(default=0, verbose_name="用户订单数量"),
                ),
                (
                    "order_amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="订单总金额",
                        default=Decimal("0"),
                    ),
                ),
                (
                    "total_used_traffic",
                    models.BigIntegerField(default=0, verbose_name="总流量GB"),
                ),
            ],
            options={
                "verbose_name": "每日记录",
                "verbose_name_plural": "每日记录",
                "ordering": ["-date"],
            },
        ),
    ]
