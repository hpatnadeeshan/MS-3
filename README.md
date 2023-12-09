# Recipehub

## Milestone Project -03 - _Data Centric Development_ - Code Institute



## User Experience

### User Stories

As a Visitor (Not Logged In):

+ I want to be able to explore recipes by cuisine.
+ I want to search for recipes based on ingredients or titles.
+ I want to be able to view the details of a recipe without logging in.


As a Registered User:

+ I want to be able to log in to the application.
+ I want to be able to log out of the application.
+ I want to be able to add a new recipe, including details like title, cuisine, ingredients, and preparation steps.
+ I want to be able to edit or delete the recipes I've added.
+ I want to be able to like recipes.
+ I want to be able to share recipes on social media.
+ I want to be able to comment on recipes.
+ I want to see how many recipes I've contributed on my profile page.
+ I want to see a list of all the recipes I've added.
+ I want the application to be responsive and easy to use on my mobile device.

Site Owner:

+ I want to see which recipes are the most popular.
+ I want users to see suggestions for my brand's kitchen tools when adding required tools to a recipe.
+ I want to be able to feature certain recipes on the homepage.


### Design



#### Colour Scheme

# Cookbook Website Color Palette

In designing the Recipe Hub website, a carefully selected color palette has been chosen to evoke a sense of warmth, freshness, and elegance. The following color scheme is applied across the website for a cohesive and visually appealing experience:

## Colors:

1. **Primary Color: #FF6347 (Tomato)**
   - This vibrant red-orange color symbolizes the richness and warmth of cooked dishes.

2. **Secondary Color: #8F9779 (Sage)**
   - A muted green reminiscent of herbs and fresh ingredients, adding a natural and earthy feel.

3. **Accent Color: #FFD700 (Gold)**
   - Used this warm gold color for highlights and call-to-action buttons, bringing a touch of elegance.

4. **Background Color: #F5F5F5 (Silver)**
   - A light, neutral grayish background enhances readability and creates a clean, modern look.

5. **Text Color: #333333 (Charcoal)**
   - A dark charcoal color is used for text, providing high contrast against the light background for easy reading.



#### Typography

# Font Family Configuration for Headings and Body

In the CSS stylesheet, the `font-family` property has been defined to ensure a consistent and visually appealing typography across different heading levels and the body of the HTML document. The chosen font stack prioritizes specific fonts while providing fallback options for compatibility across various platforms.

## Heading Levels (h1 to h6)

- **h1, .h1**
- **h2, .h2**
- **h3, .h3**
- **h4, .h4**
- **h5, .h5**
- **h6, .h6**

For the above heading levels, the following font-family hierarchy has been established:

1. **"Merriweather Sans"**: This is the preferred font for headings, providing a clean and modern appearance.

2. **-apple-system, BlinkMacSystemFont**: These are system fonts for Apple devices and Blink-based browsers, ensuring a seamless and native look on these platforms.

3. **"Segoe UI"**: A Windows system font, contributing to a consistent experience for users on Windows operating systems.

4. **Roboto**: A widely used and versatile sans-serif font that serves as a reliable fallback on various platforms.

5. **"Helvetica Neue", Arial, "Noto Sans"**: Additional sans-serif options that cater to different operating systems and browsers.

6. **sans-serif**: A generic sans-serif font to cover cases where none of the specified fonts are available.

## Body

For the overall body text of the document, the same font stack is applied, promoting a cohesive and harmonious design throughout the website.


### Wireframes

[Landing page Mobile](./recipehub/static/assets/wireframes/mobile-home.jpg)

[Recipe Explore page Mobile](./recipehub/static/assets/wireframes/mobile-recipe-explore.jpg)

[Add and Edit page Mobile](./recipehub/static/assets/wireframes/mobile-add-edit.jpg)

[profile page Mobile](./recipehub/static/assets/wireframes/mobile-profile.jpg)

[view Recipe page Mobile](./recipehub/static/assets/wireframes/mobile-recipe.jpg)

[Landing page tablet](./recipehub/static/assets/wireframes/tablet-home.jpg)

[Recipe Explore page tablet](./recipehub/static/assets/wireframes/tablet-recipe-explore.jpg)

[Add and Edit page tablet](./recipehub/static/assets/wireframes/Add-edit-recipe.jpg)

[profile page tablet](./recipehub/static/assets/wireframes/tablet-profile.jpg)

[view Recipe page tablet](./recipehub/static/assets/wireframes/tablet-recipe.jpg)

[Landing page Desktop](./recipehub/static/assets/wireframes/Home-page.jpg)

[Recipe Explore page Desktop](./recipehub/static/assets/wireframes/Recipe-Explore-page.jpg)

[Add and Edit page Desktop](./recipehub/static/assets/wireframes/Add-edit-recipe.jpg)

[profile page Desktop](./recipehub/static/assets/wireframes/profile-page.jpg)

[view Recipe page Desktop](./recipehub/static/assets/wireframes/Recipe-view-page.jpg)


## Features

### Existing Features



### Future Features


#### Share on Social Media

Allow users to share their favorite recipes on various social media platforms.

#### Recipe Comments

Enable users to leave comments on recipes to share their thoughts, tips, or modifications.

#### Instant Update for Tools and Cuisines

Implement a feature that dynamically adds new tools or cuisines to the database without requiring a page reload when added from the add or edit recipe page.

## Technologies Used

+ **Google Chrome Dev Tools:** Used for debugging.
+ **Google Lighthouse:** Utilized for audits.
+ **Git:** Source control for version management.
+ **VS Code:** Integrated Development Environment (IDE) for coding.
+ **CodeAnywhere:** Online IDE for collaborative development.
+ **W3C Validator:** Used for HTML validation.
+ **Jigsaw Validator:** Used for CSS validation.
+ **JSHint:** Used for JavaScript validation.
+ **Python Validator:** [PEP8CI](https://pep8ci.herokuapp.com/) for Python code style validation.
+ **Heroku:** Deployment platform for hosting the application.
+ **SQLAlchemy ORM:** Object-Relational Mapping for Python.
+ **ElephantSQL:** Database server for PostgreSQL.
+ **PostgreSQL:** Relational database management system.
+ **Psycopg2:** PostgreSQL adapter for Python.
+ **jQuery:** JavaScript library for simplifying HTML DOM traversal and manipulation.
+ **Flask:** Micro web framework for Python.

### Languages Used

+ HTML5
+ CSS3
+ Java Script
+ Python

### Frameworks, Libraries, and Programs Used

1. **Bootstrap Icons**
   - **Source:** [Bootstrap Icons](https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css)
  
2. **Google Fonts**
   - **Fonts:** Merriweather Sans (400, 700), Merriweather (400, 300, 300italic, 400italic, 700, 700italic)
   - **Source:** [Google Fonts](https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700) and [Google Fonts](https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic)

3. **SimpleLightbox Plugin**
   - **Version:** 2.1.0
   - **Source:** [SimpleLightbox](https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css) and [SimpleLightbox](https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js)

4. **Bootstrap**
   - **Version:** 4.6.2
   - **Source:** [Bootstrap](https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js)

5. **Font Awesome**
   - **Version:** 5 (Free)
   - **Source:** [Font Awesome](https://kit.fontawesome.com/937ad0d044.js)

6. **jQuery**
   - **Version:** 3.7.1
   - **Source:** [jQuery](https://code.jquery.com/jquery-3.7.1.js)

7. **Bootstrap Select**
   - **Version:** 1.13.1
   - **Source:** [Bootstrap Select CSS](https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.1/css/bootstrap-select.min.css) and [Bootstrap Select JS](https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.1/js/bootstrap-select.min.js)

8. **SQLAlchemy ORM**
   - **Source:** [SQLAlchemy](https://www.sqlalchemy.org/)

9. **Flask**
   - **Source:** [Flask](https://flask.palletsprojects.com/)



## Testing

### Validator Testing

Validation is done throughout the development and all the error and warnings are fixed.

following validators have been used to validate HTML and CSS codes.

### <em>HTML Validator</em>

+ [W3C validator](https://validator.w3.org/) used for HTML validating

![Html Validation](./recipehub/static/assets/validate/html.png)

### <em>CSS Validator</em>

+ [CSS validation](https://jigsaw.w3.org/css-validator/) used for CSS validation

![CSS validation](./recipehub/static/assets/validate/css-validate.png)

### <em>Java Script Validator</em>

+ [JSHint Validator](https://jshint.com/) used for CSS validation

![Java Script Validation](./recipehub/static/assets/validate/java-script.png)

### <em>Python Validator</em>

+ [PEP8CI Validator](https://pep8ci.herokuapp.com/) used for CSS validation

![Python Validation](./recipehub/static/assets/validate/routes.py-validate.png)
![Python Validation](./recipehub/static/assets/validate/models.py-validate.png)

### Responsiveness

| Page Name       | Desktop View       | Tablet View        | Mobile View        |
|-----------------|--------------------|--------------------|--------------------|
| Add Recipe      | [Link](./recipehub/static/assets/responsiveness/desktop-add-recipe.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-add-recipe.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-add-recipe.png)          |
| Edit Recipe     | [Link](./recipehub/static/assets/responsiveness/desktop-edit-recipe.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-edit-recipe.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-edit-recipe.png)          |
| Home            | [Link](./recipehub/static/assets/responsiveness/desktop-home.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-home.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-home.png)          |
| Login           | [Link](./recipehub/static/assets/responsiveness/desktop-login.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-login.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-login.png)          |
| Manage data     | [Link](./recipehub/static/assets/responsiveness/desktop-manage-data.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-manage-data.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-manage-data.png)          |
| View Messages   | [Link](./recipehub/static/assets/responsiveness/desktop-messages.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-view-recipe.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-messages.png)          |
| Profile         | [Link](./recipehub/static/assets/responsiveness/desktop-profile.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-profile.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-profile.png)          |
| Recipe Explore  | [Link](./recipehub/static/assets/responsiveness/desktop-recipe-explore.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-recipe-explore.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-recipe-explore.png)          |
| Signup          | [Link](./recipehub/static/assets/responsiveness/desktop-sign-up.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-sign-up.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-sign-up.png)          |
| View Recipe     | [Link](./recipehub/static/assets/responsiveness/desktop-view-recipe.png)          | [Link](./recipehub/static/assets/responsiveness/ipad-view-recipe.png)          | [Link](./recipehub/static/assets/responsiveness/iphone-se-view-recipe.png)          |


### Testing Accessibility and Performance

I used google lighthouse to check Accessibility and Performance.

|                    | Performance | Accessibility | Best Practices | SEO |
| ------------------ | ----------- | ------------- | -------------- | --- |
| [Add Recipe/Desktop view](./recipehub/static/assets/accessibilty/desktop-add-recipe.png)      | 97%         | 100%          | 100%           | 89% |
| [Add Recipe/Mobile view](./recipehub/static/assets/accessibilty/mobile-add-recipe.png)       | 71%         | 100%          | 100%           | 91% |
| [Edit Recipe/Desktop view](./recipehub/static/assets/accessibilty/desktop-edit-recipe.png)      | 96%         | 100%          | 100%           | 89% |
| [Edit Recipe/Mobile view](./recipehub/static/assets/accessibilty/mobile-edit-recipe.png)       | 72%         | 100%          | 100%           | 91% |
| [Home/Desktop view](./recipehub/static/assets/accessibilty/desktop-home.png)      | 84%         | 100%          | 100%           | 90% |
| [Home/Mobile view](./recipehub/static/assets/accessibilty/mobile-home.png)       | 70%         | 100%          | 100%           | 92% |
| [Login/Desktop view](./recipehub/static/assets/accessibilty/desktop-login.png)      | 91%         | 100%          | 100%           | 89% |
| [Login/Mobile view](./recipehub/static/assets/accessibilty/mobile-login.png)       | 72%         | 100%          | 100%           | 91% |
| [Manage data/Desktop view](./recipehub/static/assets/accessibilty/desktop-manage-data.png)      | 96%         | 94%          | 100%           | 89% |
| [Manage data/Mobile view](./recipehub/static/assets/accessibilty/mobile-manage-data.png)       | 64%         | 94%          | 100%           | 91% |
| [View Messages/Desktop view](./recipehub/static/assets/accessibilty/desktop-messages.png)      | 94%         | 100%          | 100%           | 89% |
| [View Messages/Mobile view](./recipehub/static/assets/accessibilty/mobile-messages.png)       | 73%         | 100%          | 100%           | 91% |
| [Profile/Desktop view](./recipehub/static/assets/accessibilty/desktop-profile.png)      | 94%         | 100%          | 100%           | 89% |
| [Profile/Mobile view](./recipehub/static/assets/accessibilty/mobile-profile.png)       | 75%         | 100%          | 100%           | 91% |
| [Recipe Explore/Desktop view](./recipehub/static/assets/accessibilty/desktop-recipe-explore.png)      | 94%         | 100%          | 100%           | 90% |
| [Recipe Explore/Mobile view](./recipehub/static/assets/accessibilty/mobile-recipe-explore.png)       | 71%         | 100%          | 100%           | 92% |
| [Signup/Desktop view](./recipehub/static/assets/accessibilty/desktop-sign-up.png)      | 96%         | 100%          | 100%           | 89% |
| [Signup/Mobile view](./recipehub/static/assets/accessibilty/mobile-sign-up.png)       | 77%         | 100%          | 100%           | 91% |
| [View Recipe/Desktop view](./recipehub/static/assets/accessibilty/desktop-view-recipe.png)      | 98%         | 100%          | 100%           | 90% |
| [View Recipe/Mobile view](./recipehub/static/assets/accessibilty/mobile-view-recipe.png)       | 77%         | 100%          | 100%           | 92% |


### Testing User Stories

#### As a Visitor (Not Logged In):

- I can explore recipes by cuisine.
- I can search for recipes based on ingredients or titles.
- I can view the details of a recipe without logging in.

#### As a Registered User:

- I can log in to the application.
- I can log out of the application.
- I can add a new recipe, including details like title, cuisine, ingredients, and preparation steps.
- I can edit or delete the recipes I've added.
- I can see how many recipes I've contributed on my profile page.
- I can see a list of all the recipes I've added.
- I can use the application on my mobile device as it is responsive and easy to navigate.

#### Site Owner:

- I can see which recipes are the most popular.
- I can present users with suggestions for my brand's kitchen tools when they add required tools to a recipe.
- I can feature certain recipes on the homepage.


### Problems Encountered



## Deployment


## Admin credentials/ Superuser credentials

+ username- admin
+ password-12345678
  
## Credits

### Code


### Media


### Acknowledgements



## Disclaimer

This project was developed for educational purposes as part of the Code Institute's Data Centric Development module.
