from django.db import models

class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    contato_nome_input = models.CharField(max_length=100)
    contato_email_input = models.EmailField(max_length=200)
    contato_telefone_input = models.CharField(max_length=16)
    contato_empresa_input = models.CharField(max_length=60)

    def __str__(self):
        return self.contato_nome_input

    class Meta:
        db_table = "contatos"
        verbose_name = 'Contato'