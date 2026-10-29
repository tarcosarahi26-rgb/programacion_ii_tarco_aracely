from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0008_alter_project_description_alter_project_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="alumno",
            old_name="create_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="estudiante",
            old_name="create_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="mision",
            old_name="create_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="participacion",
            old_name="create_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="sensei",
            old_name="create_at",
            new_name="created_at",
        ),
        migrations.CreateModel(
            name="Estacionamiento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100)),
                ("dirección", models.TextField(blank=True)),
                ("capacidad_total", models.TextField(blank=True)),
                ("espacios_disponibles", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="actividad",
            name="objetivo",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="foto",
            field=models.ImageField(upload_to="perfiles/"),
        ),
    ]