from django.db import models

class Pokemon(models.Model):
    pokemon_id = models.IntegerField(unique=False)  # Not unique because of forms like Castform
    name = models.CharField(max_length=100)
    height = models.FloatField(help_text="Height in meters")
    weight = models.FloatField(help_text="Weight in kilograms")
    types = models.CharField(max_length=200, help_text="Comma-separated types")
    family = models.CharField(max_length=100)

    class Meta:
        ordering = ['pokemon_id', 'name']
        verbose_name_plural = "Pokemon"

    def __str__(self):
        return f"#{self.pokemon_id} {self.name}"

    def get_types_list(self):
        """Returns types as a list"""
        return self.types.split(',') if self.types else []

    def get_type_badges(self):
        """Returns HTML for type badges"""
        return self.get_types_list()
