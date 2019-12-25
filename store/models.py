from django.db import models


class KeyVal(models.Model):
    key = models.CharField(max_length=511, primary_key=True)
    value = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        db_table = "key_values"
        verbose_name = "Key Value"
        verbose_name_plural = "KeyValues"