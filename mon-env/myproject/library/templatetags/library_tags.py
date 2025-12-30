from django import template
from django.utils import timezone
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def format_isbn(value):
    if len(value) == 13:
        return f"{value[:3]}-{value[3:5]}-{value[5:9]}-{value[9:12]}-{value[12]}"
    return value

@register.filter
def overdue_days(loan):
    if loan.status == 'overdue':
        return (timezone.now().date() - loan.due_date).days
    return 0

@register.simple_tag
def loan_status_badge(loan):
    if loan.status == 'borrowed':
        return mark_safe('<span class="badge bg-primary">Emprunté</span>')
    elif loan.status == 'returned':
        return mark_safe('<span class="badge bg-success">Retourné</span>')
    elif loan.status == 'overdue':
        return mark_safe('<span class="badge bg-danger">En retard</span>')
    return mark_safe('<span class="badge bg-secondary">Inconnu</span>')

@register.simple_tag
def calculate_penalty_tag(loan):
    return loan.calculate_penalty()

@register.inclusion_tag('library/components/book_card.html')
def book_card(book):
    return {'book': book}