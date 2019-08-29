from django.db import models


class PrimerModulo(models.Model):
    MINIMO = 1
    POCO = 2
    BASTANTE = 3
    TOTALMENTE = 4
    BAJA = 5
    ALTA = 6
    SUPERIOR = 7

    PRIMERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (TOTALMENTE, 'TOTALMENTE'),
    )

    SEGUNDA_LISTA = (
        (MINIMO, 'MINIMO'),
        (BAJA, 'BAJA'),
        (ALTA, 'ALTA'),
        (SUPERIOR, 'SUPERIOR'),
    )

    respuestaPregunta1 = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                          verbose_name='1. ¿Qué tanto sabe para resolver este problema?')
    respuestaPregunta2 = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                          verbose_name='2. ¿Conoce estrategias para resolver este problema?"')
    respuestaPregunta3 = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                          verbose_name='3. ¿Qué tanto sirve el plan que tiene para resolver este problema? ')
    respuestaPregunta4 = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                          verbose_name='4. ¿Qué conocimientos tiene sobre los temas relacionados con la solución de problemas? ')
    respuestaPregunta5 = models.PositiveSmallIntegerField(choices=SEGUNDA_LISTA,
                                                          verbose_name='5. El valor de la meta que se ha propuesto es:')
    timestamp = models.DateField(auto_now_add=True, auto_now=False)


class ModuloDuranteUno(models.Model):
    MINIMO = 1
    POCO = 2
    BASTANTE = 3
    TOTALMENTE = 4

    PRIMERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (TOTALMENTE, 'TOTALMENTE'),
    )

    respuestaPregunta = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                         verbose_name='6. ¿Si no comprende el problema tiene algún plan para encontrar la solución? Indique el nivel de precisión.')
    timestamp = models.DateField(auto_now_add=True, auto_now=False)


class ModuloDuranteDos(models.Model):
    MINIMO = 1
    POCO = 2
    BASTANTE = 3
    TOTALMENTE = 4
    MUCHO = 5

    PRIMERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (MUCHO, 'MUCHO'),
    )

    respuestaPregunta = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                         verbose_name='7. El tiempo que puede durar solucionando el problema es:')
    timestamp = models.DateField(auto_now_add=True, auto_now=False)


class ModuloDuranteTres(models.Model):
    MINIMO = 1
    POCO = 2
    BASTANTE = 3
    TOTALMENTE = 4

    PRIMERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (TOTALMENTE, 'TOTALMENTE'),
    )

    respuestaPregunta = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                         verbose_name='8. ¿Qué tanto uso las estrategias que planeo en la solución de problemas?')
    timestamp = models.DateField(auto_now_add=True, auto_now=False)


class ModuloDuranteCuatro(models.Model):
    MINIMO = 1
    POCO = 2
    BASTANTE = 3
    TOTALMENTE = 4

    PRIMERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (TOTALMENTE, 'TOTALMENTE'),
    )

    respuestaPregunta = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                         verbose_name='9.¿Que tanto replanteo sus estrategias y uso unas  nuevas?')
    timestamp = models.DateField(auto_now_add=True, auto_now=False)


class ModuloDuranteCinco(models.Model):
    MINIMO = 1
    POCO = 2
    BASTANTE = 3
    TOTALMENTE = 4

    PRIMERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (TOTALMENTE, 'TOTALMENTE'),
    )

    respuestaPregunta = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                         verbose_name='10. ¿En qué nivel considero que estoy logrando la solución del problema?')
    timestamp = models.DateField(auto_now_add=True, auto_now=False)


class Final(models.Model):
    MINIMO = 1
    POCO = 2
    BASTANTE = 3
    TOTALMENTE = 4
    BAJA = 5
    ALTA = 6
    SUPERIOR = 7
    MUCHO = 8

    PRIMERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (TOTALMENTE, 'TOTALMENTE'),
    )

    SEGUNDA_LISTA = (
        (MINIMO, 'MINIMO'),
        (BAJA, 'BAJA'),
        (ALTA, 'ALTA'),
        (SUPERIOR, 'SUPERIOR'),
    )
    TERCERA_LISTA = (
        (MINIMO, 'MINIMO'),
        (POCO, 'POCO'),
        (BASTANTE, 'BASTANTE'),
        (MUCHO, 'MUCHO'),
    )

    respuestaPregunta11 = models.PositiveSmallIntegerField(choices=TERCERA_LISTA,
                                                           verbose_name='11. ¿Qué nivel de conocimiento ha alcanzado  con la soluciones que ha realizado hasta el momento?')
    respuestaPregunta12 = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                           verbose_name='12. ¿Qué  tanto uso las ayudas para resolver  los problemas?')
    respuestaPregunta13 = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                           verbose_name='13. ¿Qué tanto he aprendido en la solución de problemas?')
    respuestaPregunta14 = models.PositiveSmallIntegerField(choices=PRIMERA_LISTA,
                                                           verbose_name='14. ¿En que nivel alcance la meta propuesta al iniciar con la solución de problemas?')

    timestamp = models.DateField(auto_now_add=True, auto_now=False)
