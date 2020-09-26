from django.core.paginator import Paginator
from django.db import OperationalError, connection, transaction
from django.utils.functional import cached_property


class TimeLimitedPaginator(Paginator):
    """
    Paginator that does not count the rows in the table.
    """

    @cached_property
    def count(self):
        # We set the timeout in a db transaction to prevent it from
        # affecting other transactions.
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.execute("SET LOCAL statement_timeout TO 200;")
            try:
                return super(TimeLimitedPaginator, self).count
            except OperationalError:
                return self._get_fuzzy_count()

    def _get_fuzzy_count(self):
        query = self.object_list.query
        if not query.where:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT reltuples FROM pg_class WHERE relname = %s",
                        [query.model._meta.db_table],
                    )
                    return int(cursor.fetchone()[0])
            except Exception as e:
                print(("Exception:::Exception", str(e)))
                return 9999999999

        return 9999999999
