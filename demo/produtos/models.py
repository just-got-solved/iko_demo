from django.db import models


class ProdutoConcorrenteIna(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "prod_concorrencia_ina"
        verbose_name = 'Produto INA'

class ProdutoConcorrenteSkf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "prod_concorrencia_skf"
        verbose_name = 'Produto SKF'

class ProdutoConcorrenteFag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "prod_concorrencia_fag"
        verbose_name = 'Produto FAG'

class ProdutoConcorrenteTorrington(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "prod_concorrencia_torrington"
        verbose_name = 'Produto Torrington'


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    dimensions_fw = models.IntegerField()
    dimensions_d = models.IntegerField()
    dimensions_c = models.IntegerField()
    basic_dyn_load_rat = models.CharField(max_length=100)
    basic_static_load_rat = models.CharField(max_length=100)
    usable_inn_rng = models.CharField(max_length=100)
    produto_ina = models.ForeignKey(ProdutoConcorrenteIna, on_delete=models.DO_NOTHING, to_field="id", related_name='produtos_ina')
    produto_skf = models.ForeignKey(ProdutoConcorrenteSkf, on_delete=models.DO_NOTHING, to_field="id", related_name='produtos_skf')
    produto_fag = models.ForeignKey(ProdutoConcorrenteFag, on_delete=models.DO_NOTHING, to_field="id", related_name='produtos_fag')
    produto_torrington = models.ForeignKey(ProdutoConcorrenteTorrington, on_delete=models.DO_NOTHING, to_field="id", related_name='produtos_torrington')
    
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "produtos"
        verbose_name = 'Produto'