def filter_by_user(queryset, request):
    """
    Filter querysets by the current user
    """

    return queryset.filter(user=request.user)


def filter_by_fields(queryset, category, difficulty):
    """
    Filter querysets by category or difficulty
    """

    if category:
        queryset = queryset.filter(categoria__id=category)

    if difficulty:
        queryset = queryset.filter(dificuldade=difficulty)

    return queryset
