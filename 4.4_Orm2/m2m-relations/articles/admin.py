from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, ModelForm
from .models import Article, Section, ArticleSection
from django import forms

class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_sections_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_sections_count += 1
        if main_sections_count != 1:
            raise ValidationError('Укажите один и только один основной раздел')
        return super().clean()


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    extra = 1
    formset = ArticleSectionInlineFormset


class ArticleForm(ModelForm):
    sections = forms.ModelMultipleChoiceField(queryset=Section.objects.all())

    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['sections'].initial = self.instance.sections.all()

    def save(self, commit=True):
        article = super().save(commit=False)
        if commit:
            article.save()
        if article.pk:
            article.sections.set(self.cleaned_data['sections'])
            for section in self.cleaned_data['sections']:
                article_section, created = ArticleSection.objects.get_or_create(article=article, section=section)
                article_section.is_main = section == self.cleaned_data['sections'][0]
                article_section.save()
        return article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]
    form = ArticleForm


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
