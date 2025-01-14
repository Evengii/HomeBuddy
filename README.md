# HomeBuddy test assignment
The project is created to cover the main functional user scenarios.

Test scenarios:
1. User performs an HVAC estimation by entering the zip code and going to the final thank you page.
2. User cancels HVAC estimation through the process.
3. User disagrees with constructor's conditions and cancels HVAC estimation.

# Main features
POM structure is used in the framework to provide clear structure and maintainability. 

The idea of `locators` folder is to store locators in different files according to project type (Siding, Roofing, etc.) with the ability to expand locator's classes and add other project types. There is also `common` file to store locators which appear for all project types.
Specific locators and methods are stored in `pages` folder to isolate internal page methods from the tests. 
To keep data diversity Faker lib is used to fill user info fields.
