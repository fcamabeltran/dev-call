from django.db import models

class Respaldo(models.Model):
  Tabla = models.CharField(primary_key=True,max_length=30,db_column='bcab_tabla')
  Base = models.CharField(primary_key=True,max_length=20,db_column='bcab_base')
  Rutaoutput = models.CharField(max_length=100, blank=True, null=True,db_column='bcab_rutaoutput')
  Prefijooutput = models.CharField(max_length=30, blank=True, null=True,db_column='bcab_prefijooutput')
  Campoclave = models.CharField(max_length=30, blank=True, null=True,db_column='bcab_campoclave')
  Diasreten_bd = models.BigIntegerField(blank=True, null=True,db_column='bcab_diasreten_bd')
  Diasreten_fs = models.BigIntegerField(blank=True, null=True,db_column='bcab_diasreten_fs')
  Claveminimaactual = models.DateField(blank=True, null=True,db_column='bcab_claveminimaactual')
  flg_backup = models.NullBooleanField(db_column='bcab_flg_backup')
  Maxdiasbackup = models.BigIntegerField(blank=True, null=True,db_column='bcab_maxdiasbackup')
  Ultimodiabackup = models.DateField(blank=True, null=True,db_column='bcab_ultimodiabackup')
  Flg_delete = models.NullBooleanField(db_column='bcab_flg_delete')
  Maxdiasdelete = models.BigIntegerField(blank=True, null=True,db_column='bcab_maxdiasdelete')
  Ultimodiadelete = models.DateField(blank=True, null=True,db_column='bcab_ultimodiadelete')
  Procedure = models.CharField(max_length=30, blank=True, null=True,db_column='bcab_procedure')
  Flg_estado = models.NullBooleanField(db_column='bcab_flg_estado' )
  def __str__(self):
    return self.Rutaoutput 
  class Meta:
    managed = False
    db_table = 'TIWS_BACKUP_CAB'