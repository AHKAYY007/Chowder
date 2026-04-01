from langchain.tools import tool


@tool
async def fetch_food():
    """Fetch food from the menu."""
    ...


@tool
async def make_payment():
    """Make a payment for the order."""
    ...


@tool
async def log_action():
    """log action to kite blockchain."""
    ...