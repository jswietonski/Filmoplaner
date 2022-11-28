from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, groups_names):
    if groups_names is None:
        return False
    grupy = [group.strip() for group in groups_names.split(',')]
    for grupa in grupy:
        if user.groups.filter(name=grupa).exists():
            return True
    return False