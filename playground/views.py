from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

# Create your views here.


def say_hello(request):
    # collection = Collection(pk=11)
    # collection.delete()

    Collection.objects.filter(id__gt=12).delete()

    # collection = Collection.object.get(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()

    # Problem with changing names of for example "Freatured_product" but no pre loading needed so faster
    # Collection.objects.filter(pk=11).update(featured_product=None)

    # quaryset = Product.objects.all()
    # writes to quaryset cache
    # list(quaryset)
    # gets from cache
    # list(quaryset)

    # TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'name': 'timo', 'tags': list()})
