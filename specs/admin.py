from django.contrib import admin
from specs.models import (
    CategoryFeature,
    ProductFeature,
    FeatureValidator
)

admin.site.register(CategoryFeature)
admin.site.register(ProductFeature)
admin.site.register(FeatureValidator)