from django.db import models

class Usuarios(models.Model):
    usuario = models.CharField(max_length=45)
    email = models.EmailField()
    senha = models.CharField(max_length=45)

    def __str__(self):
        return self.usuario

class Livros(models.Model):
    isbn = models.CharField(primary_key=True, max_length=45)
    titulo = models.CharField(max_length=45)
    autor = models.CharField(max_length=45)
    ano = models.IntegerField()
    genero = models.CharField(max_length=45)

    def __str__(self):
        return self.titulo

class Resenhas(models.Model):
    texto = models.TextField()
    data = models.DateField()
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.livro

class Avaliacao(models.Model):
    pontuacao = models.IntegerField()
    comentario = models.TextField()
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.pontuacao

