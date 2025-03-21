# Generated by Django 5.0.3 on 2024-04-10 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anamnesis', models.TextField(max_length=800, null=True, verbose_name='Anamnesis')),
                ('motivo_consulta', models.TextField(blank=True, max_length=500, null=True, verbose_name='Motivo de Consulta')),
                ('alergias', models.TextField(max_length=800, null=True, verbose_name='Alergias')),
                ('enfermedades_anteriores', models.TextField(max_length=800, null=True, verbose_name='Enfermedades Anteriores')),
                ('antescedentes_familiares', models.TextField(max_length=800, null=True, verbose_name='Antescedentes Familiares')),
                ('cirugias', models.TextField(max_length=800, null=True, verbose_name='Cirugia')),
                ('estado_reproductivo', models.CharField(max_length=150, null=True, verbose_name='Estado Reproductivo')),
                ('alimentacion', models.CharField(max_length=150, null=True, verbose_name='Alimentacion')),
                ('habitat', models.CharField(max_length=150, null=True, verbose_name='Habitat')),
                ('tllc', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='TLLC')),
                ('pulso', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Pulso')),
                ('fc', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='FC')),
                ('fr', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='FR')),
                ('temperatura', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Temperatura')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Peso')),
                ('actitud', models.CharField(max_length=150, null=True, verbose_name='Actitud')),
                ('condicion_corporal', models.CharField(max_length=150, null=True, verbose_name='Condicion Corporal')),
                ('hidratacion', models.CharField(max_length=150, null=True, verbose_name='Hidratacion')),
                ('interpretacion_resultados', models.TextField(blank=True, max_length=500, null=True, verbose_name='Interpretacion Resultados')),
                ('impresion_diagnostica', models.TextField(blank=True, max_length=500, null=True, verbose_name='Impresion Diagnostico')),
                ('estado', models.CharField(blank=True, max_length=20, null=True, verbose_name='Estado de la mascota')),
            ],
            options={
                'verbose_name': 'Ecop',
                'verbose_name_plural': 'Ecops',
                'db_table': 'ecop',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre de la Mascota')),
                ('especie', models.CharField(blank=True, max_length=60, null=True, verbose_name='Especie de la Mascota')),
                ('raza', models.CharField(blank=True, max_length=60, null=True, verbose_name='Raza de la Mascota')),
                ('edad', models.IntegerField(blank=True, null=True, verbose_name='Edad de la Mascota')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Color de la Mascota')),
                ('sexo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Sexo de la Mascota')),
                ('chip', models.CharField(blank=True, max_length=50, null=True, verbose_name='Chip de la Mascota')),
                ('tipo_consulta', models.TextField(blank=True, max_length=500, null=True, verbose_name='Motivo de Consulta')),
                ('observacion_urgencia', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observacion Urgencia')),
                ('fecha_consulta', models.DateField(verbose_name='Fecha de consulta')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'db_table': 'mascota',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tutor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del Tutor')),
                ('dni', models.CharField(blank=True, max_length=100, null=True, verbose_name='Identidad del Tutor')),
                ('direccion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Direccion del Tutor')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Contacto del Tutor')),
            ],
            options={
                'verbose_name': 'Tutor',
                'verbose_name_plural': 'Tutores',
                'db_table': 'tutor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_examen', models.CharField(blank=True, max_length=80, null=True, verbose_name='Diagnostico')),
                ('autorizado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Autorizacion')),
                ('laboratorio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Laboratorio')),
                ('resultados', models.TextField(blank=True, max_length=500, null=True, verbose_name='Resultados')),
                ('fecha', models.DateField(verbose_name='Fecha del Diagnostico')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Diagnostico',
                'verbose_name_plural': 'Diagnosticos',
                'db_table': 'diagnostico',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Desparacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Producto')),
                ('fecha', models.DateTimeField(verbose_name='Fecha de Desparacitacion')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Desparacitacion',
                'verbose_name_plural': 'Desparacitaciones',
                'db_table': 'desparacitacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Autorizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre del Autorizado')),
                ('dni', models.CharField(blank=True, max_length=100, null=True, verbose_name='Documento de Identidad')),
                ('semestre', models.IntegerField(blank=True, null=True, verbose_name='Semestre del Estudiante')),
                ('firma', models.ImageField(blank=True, upload_to='firmas')),
                ('ecop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='domain.ecop')),
            ],
            options={
                'verbose_name': 'Autorizado',
                'verbose_name_plural': 'Autorizados',
                'db_table': 'autorizado',
            },
        ),
        migrations.AddField(
            model_name='ecop',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.mascota'),
        ),
        migrations.CreateModel(
            name='Mucosa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rectal', models.BooleanField(blank=True, default=True, null=True, verbose_name='Mucosa Rectal')),
                ('conjuntival', models.BooleanField(blank=True, default=True, null=True, verbose_name='Mucosa Conjuntival')),
                ('vulvar_prepucial', models.BooleanField(blank=True, default=True, null=True, verbose_name='Mucosa Vulvar o Prepucial')),
                ('observacion_rectal', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observacion')),
                ('observacion_conjuntival', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observacion')),
                ('observacion_vulvar_prepucial', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observacion')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Mucosa',
                'verbose_name_plural': 'Mucosas',
                'db_table': 'mucosa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nodulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(blank=True, default=True, null=True, verbose_name='Estado')),
                ('observacion_nodulos', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observacion')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Nodulos',
                'verbose_name_plural': 'Nodulos',
                'db_table': 'nodulos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problema', models.CharField(blank=True, max_length=80, null=True, verbose_name='Problema')),
                ('maestra', models.CharField(blank=True, max_length=100, null=True, verbose_name='Maestra')),
                ('diagnostico_diferencial', models.TextField(blank=True, max_length=500, null=True, verbose_name='Diagnostico Diferencial')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Problema',
                'verbose_name_plural': 'Problemas',
                'db_table': 'problema',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema', models.CharField(blank=True, max_length=80, null=True, verbose_name='Nombre del Sistema')),
                ('organo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Organo')),
                ('enfermedad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Enfermedad')),
                ('observacion', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observacion')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'db_table': 'sistema',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Terapia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tratamiento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tratamiento')),
                ('principio_activo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Principio Activo')),
                ('presentacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Presentacion')),
                ('posologia', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Posologia')),
                ('dosis_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Dosis Total')),
                ('via', models.CharField(blank=True, max_length=100, null=True, verbose_name='Via de Tratamiento')),
                ('frecuencia', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Frecuencia de Tratamiento')),
                ('duracion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Duracion del Tratamiento')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Terapia',
                'verbose_name_plural': 'Terapias',
                'db_table': 'terapia',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='mascota',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='domain.tutor', verbose_name='Tutor de la mascota'),
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_vacuna', models.CharField(max_length=150, null=True, verbose_name='Tipo de vacunacion')),
                ('producto', models.CharField(max_length=150, null=True, verbose_name='Producto')),
                ('fecha', models.DateField(verbose_name='Fecha de Vacunacion')),
                ('ecop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.ecop', verbose_name='Ecop')),
            ],
            options={
                'verbose_name': 'Vacunacion',
                'verbose_name_plural': 'Vacunaciones',
                'db_table': 'vacunacion',
                'managed': True,
            },
        ),
    ]
