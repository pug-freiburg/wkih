def test_home_view():
    """ The home view is rendered using bootstrap."""

    from app import home_view, app as app_
    with app_.app_context():
        home_html = home_view()

    assert "Theme Template for Bootstrap" in home_html


def test_project_api():
    """ the project api returns a list of projects on get """

    from app import project_api

    assert project_api() == []
