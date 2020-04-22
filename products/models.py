from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        # --------------------------------------------------->
        #
        #   IMPORTANT!
        #     Reverse method searches the first parameter given,
        #     (in this case: product_detail) inside the app
        #     urls.py (in this case /src/trydjango/urls.py) and
        #     selects the specific url that matches given name!
        #     Also a namespace can be specified (in this case
        #     products:...) in order to specify which set of
        #     will be searched first if 2 urls have the same name
        #
        # --------------------------------------------------->
        return reverse('products:product_detail', kwargs={'id': self.id})
