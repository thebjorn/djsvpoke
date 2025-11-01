from django.shortcuts import render
from django.db.models import Q
from .models import Pokemon


def pokemon_list(request):
    # Start with all Pokemon
    pokemon = Pokemon.objects.all()

    # Get filter/search parameters
    search_query = request.GET.get('search', '')
    type_filter = request.GET.get('type', '')
    family_filter = request.GET.get('family', '')
    sort_by = request.GET.get('sort', 'pokemon_id')

    # Apply search
    if search_query:
        pokemon = pokemon.filter(
            Q(name__icontains=search_query) |
            Q(types__icontains=search_query) |
            Q(family__icontains=search_query)
        )

    # Apply type filter
    if type_filter:
        pokemon = pokemon.filter(types__icontains=type_filter)

    # Apply family filter
    if family_filter:
        pokemon = pokemon.filter(family__iexact=family_filter)

    # Apply sorting
    valid_sort_fields = ['pokemon_id', '-pokemon_id', 'name', '-name',
                         'height', '-height', 'weight', '-weight']
    if sort_by in valid_sort_fields:
        pokemon = pokemon.order_by(sort_by)

    # Get unique types and families for filter dropdowns
    all_pokemon = Pokemon.objects.all()
    all_types = set()
    all_families = set()

    for p in all_pokemon:
        all_types.update(p.get_types_list())
        all_families.add(p.family)

    context = {
        'pokemon_list': pokemon,
        'search_query': search_query,
        'type_filter': type_filter,
        'family_filter': family_filter,
        'sort_by': sort_by,
        'all_types': sorted(all_types),
        'all_families': sorted(all_families),
        'total_count': pokemon.count(),
    }

    return render(request, 'pokemon/pokemon_list.html', context)
