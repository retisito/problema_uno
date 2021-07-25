from archives.models import File, Data


def run():
    Data.objects.all().delete()
    File.objects.all().delete()