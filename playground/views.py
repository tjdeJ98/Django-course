from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

# Create your views here.


def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)

    quaryset = TaggedItem.objects \
        .select_related('tag') \
        .filter(
            content_type=content_type,
            object_id=1
        )
    return render(request, 'hello.html', {'name': 'timo', 'tags': list(quaryset)})