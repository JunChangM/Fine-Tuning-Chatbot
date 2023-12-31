from django.contrib import admin
from .models import FineTunedModel, TrainingData

# Register your models here.
@admin.register(FineTunedModel)
class FineTunedModelAdmin(admin.ModelAdmin):
    list_display = ['model_name','base_model']
    search_fields = ['model_name','base_model']

@admin.register(TrainingData)
class TrainingDataAdmin(admin.ModelAdmin):
    list_display = ['prompt','completion','fine_tuned_model']
    search_fields = ['prompt','completion','fine_tuned_model_model_name']
    list_filter = ['fine_tuned_model']

