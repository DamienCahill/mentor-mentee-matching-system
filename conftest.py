import pytest
import app as webapp
import controllers.questionnaire_controller
import controllers.auth_controller
import controllers.mentor_controller
import controllers.mentoring_categories_controller
import controllers.dashboard_controller
import controllers.admin_controller
import controllers.matches_controller

@pytest.fixture
def app():
    """
    This fixture creates the client object before each test runs, assuming the test references the client object
    """
    app = webapp.app
    return app