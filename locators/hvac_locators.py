from selenium.webdriver.common.by import By

class EnergySourceLocators:
    GAS_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-energysource-gas]")
    # ...other elements on the page...

class ProjectTypeLocators:
    REPLACEMENT_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-projecttype-replacementorinstallation]")
    REPAIR_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-projecttype-repair]")
    # ...other elements on the page...

class PropertyTypeLocators:
    ROW_HOUSE_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-propertytype-detached]")
    # ...other elements on the page...

class EquipmentLocators:
    AIR_CONDITIONER_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-equipment-airconditioner]")
    CENTRAL_HEATING_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-equipment-heatingorfurnace]")
    # ...other elements on the page...

class EquipmentAgeLocators:
    LESS_THAN_5_YEARS_BUTTON = (By.CSS_SELECTOR, "input[data-autotest-equipmentage-5]")
    # ...other elements on the page...