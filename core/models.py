
from django.db import models
from  stdimage.models import   StdImageField
from  django.db.models  import  signals
from  django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('data de criação',auto_now_add=True)
    modificado = models.DateField('data de atualização',auto_now=True)
    ativo =  models.BooleanField('ativo?', default=True)

    class Meta:
        abstract = True
        
class Produto(Base):
    nome = models.CharField('nome',max_length=100)
    preco = models.DecimalField('preço',max_digits=8,decimal_places=2)
    estoque = models.IntegerField( 'estoque')
    imagem = StdImageField('imagem',upload_to='produtos',variations={'thumb':(124,124)})
    slug= models.SlugField('slug', max_length=100,blank=True, editable=False )

 
    def __str__(self):
        return self.nome
    

def produto_pre_save(signal , instance, sender , **kwargs):
        instance.slug = slugify(instance.nome)
    
signals.pre_save.connect(produto_pre_save, sender=Produto)