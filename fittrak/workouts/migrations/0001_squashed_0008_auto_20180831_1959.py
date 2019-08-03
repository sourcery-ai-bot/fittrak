# Generated by Django 2.0.7 on 2018-08-31 20:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("workouts", "0001_initial"),
        ("workouts", "0002_auto_20180509_0000"),
        ("workouts", "0003_auto_20180711_1636"),
        ("workouts", "0004_auto_20180711_1639"),
        ("workouts", "0003_auto_20180711_2121"),
        ("workouts", "0005_merge_20180711_2123"),
        ("workouts", "0006_auto_20180714_2008"),
        ("workouts", "0007_auto_20180819_1649"),
        ("workouts", "0008_auto_20180831_1959"),
    ]

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Exercise",
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
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date_started", models.DateTimeField(blank=True, null=True)),
                ("date_ended", models.DateTimeField(blank=True, null=True)),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        help_text="A human easy to read/share name for exercise",
                        max_length=15,
                        null=True,
                        unique=True,
                    ),
                ),
            ],
            options={"ordering": ("-id",)},
        ),
        migrations.CreateModel(
            name="ExerciseType",
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
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=250, unique=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Set",
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
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date_started", models.DateTimeField(blank=True, null=True)),
                ("date_ended", models.DateTimeField(blank=True, null=True)),
                ("repetitions", models.PositiveIntegerField()),
                ("weight", models.PositiveIntegerField()),
                (
                    "unit",
                    models.CharField(
                        choices=[("KG", "Kilograms"), ("LB", "Pounds")],
                        default="LB",
                        max_length=32,
                    ),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sets",
                        to="workouts.Exercise",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ("-id",)},
        ),
        migrations.CreateModel(
            name="Workout",
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
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date_started", models.DateTimeField(blank=True, null=True)),
                ("date_ended", models.DateTimeField(blank=True, null=True)),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        help_text="A human easy to read/share name for workout",
                        max_length=15,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("IN_PROGRESS", "In Progress"),
                            ("CANCELLED", "Cancelled"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="PENDING",
                        max_length=32,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ("-id",)},
        ),
        migrations.AddField(
            model_name="exercise",
            name="exercise_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="workouts.ExerciseType"
            ),
        ),
        migrations.AddField(
            model_name="exercise",
            name="workout",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exercises",
                to="workouts.Workout",
            ),
        ),
        migrations.AddField(
            model_name="exercise",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="MuscleGroup",
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
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=250, unique=True)),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="exercisetype",
            name="muscle_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="workouts.MuscleGroup",
            ),
        ),
    ]
