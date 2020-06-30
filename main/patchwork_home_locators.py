from selenium.webdriver.common.by import By

class PatchworkHomeLocators: 

    SHOW_PATCH_FILTERS = (By.LINK_TEXT, "Show patches with")

    HOME_ICON = (By.CLASS_NAME, "navbar-brand")

    FILTER_FORM = (By.ID, "filterform")

    BUNDLES = (By.PARTIAL_LINK_TEXT, "Bundles")

    PROJECT_INFORMATION = (By.PARTIAL_LINK_TEXT, "About this project")

    LOGIN = (By.LINK_TEXT, "Login")

    REGISTER = (By.LINK_TEXT, "Register")

    MAIL_SETTINGS = (By.LINK_TEXT, "Mail Settings")

