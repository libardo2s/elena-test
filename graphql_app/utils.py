from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# First we create a little helper function, becase we will potentially have many PaginatedTypes
# and we will potentially want to turn many querysets into paginated results:

def get_paginator(query, page_size, page, paginated_type, **kwargs):
    paginator = Paginator(query, page_size)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return paginated_type(
        page=page_obj.number,
        pages=paginator.num_pages,
        has_next=page_obj.has_next(),
        has_prev=page_obj.has_previous(),
        objects=page_obj.object_list,
        **kwargs
    )
