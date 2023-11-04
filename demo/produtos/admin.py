from django.contrib import admin
from .models import Produto, ProdutoConcorrenteFag, ProdutoConcorrenteIna, ProdutoConcorrenteSkf, ProdutoConcorrenteTorrington
# Register your models here.

admin.site.register([Produto,ProdutoConcorrenteFag,ProdutoConcorrenteIna,ProdutoConcorrenteSkf,ProdutoConcorrenteTorrington])
