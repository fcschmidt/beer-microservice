from beers.app.blueprints.api.utils import serializer


class Search:

    def __init__(self, query, search_item):
        self.query = query
        self.search_item = search_item

    def start_beer_serializer(self):
        beers = serializer(self.query)
        resp = self.search_beer_item(beers)
        return resp

    def search_beer_item(self, beers):
        search_list = []
        for beer in beers:
            if self.search_item in beer['beer_name']:
                search_list.append(beer)
                break

            if self.search_item in beer['color']:
                search_list.append(beer)

            if self.search_item in beer['alcohol']:
                search_list.append(beer)
                if search_list[0]['id'] == beer['id']:
                    continue

            if self.search_item in beer['temperature']:
                search_list.append(beer)
                if search_list[0]['id'] == beer['id']:
                    continue

            if self.search_item in beer['ingredients']:
                search_list.append(beer)
        return search_list
