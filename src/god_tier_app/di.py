"""DI module which setup a Wireup container for the app."""

from wireup import create_async_container

import god_tier_app.services

container = create_async_container(service_modules=[god_tier_app.services])
