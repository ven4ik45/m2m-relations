from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tags


class ArticleScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):

        main_num = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    main_num += 1
                else:
                    pass
            else:
                pass

        if main_num == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_num >= 2:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = Scope
    formset = ArticleScopeInlineFormSet
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Tags)
class Tag(admin.ModelAdmin):
    pass
