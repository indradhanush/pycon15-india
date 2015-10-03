# System imports
from datetime import (
    datetime,
    timedelta
)

# Django imports
from django.test import TestCase

# Third party imports
from freezegun import freeze_time
import pytz

# Local imports
from app.models import AccessKey


def expire_keys_older_than_30_days():
    limit = datetime.now(pytz.utc) - timedelta(days=30)
    old_keys = AccessKey.objects.filter(created_at__lte=limit)
    old_keys.update(expired=True)


class TestDeleteOlderKeys(TestCase):

    def test_expire_keys_older_than_30_days(self):
        with freeze_time('2015-1-1 00:00:00+00:00'):
            AccessKey.objects.create()

        with freeze_time('2015-1-31 00:00:00+00:00'):
            AccessKey.objects.create()

        live_keys = AccessKey.objects.filter(expired=False)

        self.assertEqual(live_keys.count(), 2)

        with freeze_time('2015-3-1 00:00:00+00:00'):
            expire_keys_older_than_30_days()

        live_keys = AccessKey.objects.filter(expired=False)
        self.assertEqual(live_keys.count(), 1)
