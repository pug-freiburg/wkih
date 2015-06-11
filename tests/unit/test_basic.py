def test_home_view():
    """Accessing the home view."""
    from app import home
    assert home() == 'Wie kann ich helfen?'
