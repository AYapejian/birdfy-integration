"""Constants for the Birdfy integration."""

DOMAIN = "birdfy"

# Netvue runs a separate API host and media bucket per AWS region, and an
# account only answers on the region it was created in — querying another
# region's host yields 403/404 rather than a redirect. Upstream hardcoded
# eu-central-1, which breaks every non-EU account.
CONF_REGION = "region"
DEFAULT_REGION = "eu-central-1"


def api_base(region: str) -> str:
    """Return the Netvue API base URL for a region."""
    return f"https://{region}-api2.nvts.co"
