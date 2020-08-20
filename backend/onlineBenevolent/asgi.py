import os
from pathlib import Path

from django.core.asgi import get_asgi_application


# This allows easy placement of apps within the interior backend directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# sys.path.append(str(ROOT_DIR / "backend"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()
