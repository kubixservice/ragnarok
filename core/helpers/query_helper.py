class QueryHelper(object):

    @staticmethod
    def validate_ordering(ordering, fields):
        if ordering:
            ordering = ordering.split(',')
            to_exclude = []

            if len(ordering) > 0:
                for x, order in enumerate(ordering):
                    if order.replace('-', '') not in fields.keys():
                        to_exclude.append(order)

            for exclude in to_exclude:
                ordering.remove(exclude)
        return ordering
