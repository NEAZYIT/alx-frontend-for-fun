# Curriculum Short Specializations - Flexbox

**HTML/CSS - Front-end**

## Description

For the "Flexbox" project, you will be applying your knowledge of the Flexbox layout module in CSS to create flexible and responsive designs. This project covers various aspects of Flexbox, including flex containers, flex items, alignment, direction, ordering, and more.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 18.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the project directory is mandatory
- Your code should follow the `W3C standards` and meet the `HTML validator` and `CSS validator` requirements

## Table of Contents

- [0. Add display flex](#0-add-display-flex)
- [1. Add new classes on sections](#1-add-new-classes-on-sections)
- [2. Reverse order Latest news cards](#2-reverse-order-latest-news-cards)
- [3. Simplify services list](#3-simplify-services-list)
- [4. Playing around with the spacing between flex service items](#4-playing-around-with-the-spacing-between-flex-service-items)
- [5. Flexify the header](#5-flexify-the-header)
- [6. Flexify the navbar](#6-flexify-the-navbar)
- [7. Align center logo and navbar](#7-align-center-logo-and-navbar)
- [8. Simplify the hero banner](#8-simplify-the-hero-banner)
- [9. Better alignment about us](#9-better-alignment-about-us)
- [10. Creating an article by fixing issues and updating hero styles](#10-creating-an-article-by-fixing-issues-and-updating-hero-styles)
- [11. Update the new hero banner](#11-update-the-new-hero-banner)
- [12. The structure of the main article](#12-the-structure-of-the-main-article)
- [13. The meta list inside the aside section](#13-the-meta-list-inside-the-aside-section)
- [14. Add the share social icons](#14-add-the-share-social-icons)
- [15. Finalizing the cherry on the cake that is the article](#15-finalizing-the-cherry-on-the-cake-that-is-the-article)
- [16. Timemachine boxes!](#16-timemachine-boxes)

### 0. Add display flex

**[Mandatory]**

Use the provided starter HTML and CSS files for this task. When using `display: flex;` on a container, all direct children become flex items (and no more inline or block elements).

In the `/* Grid` section within your CSS, add a selector for the `row` class and set the `display` property to `flex`. This will make all children of the `row` class flex items.

Entirely remove the `row::after` declaration and the `float: left` inside `[class*='col-']`. All elements should appear the same as before, but using Flexbox instead of floats.

### 1. Add new classes on sections

**[Mandatory]**

Using the files from the previous task as the base, add the following classes to the respective sections:

- `section-services` to the outermost section tag for services
- `section-works` to the outermost section tag for works
- `section-about-us` to the outermost section tag for about
- `section-latest-news` to the outermost section tag for latest_news
- `section-testimonial` to the outermost section tag for testimonial
- `section-contact` to the outermost section tag for contact

### 2. Reverse order Latest news cards

**[Mandatory]**

Using the files from the previous task, target the `row` class inside the `section-latest-news` class and set the `flex-direction` property to `row-reverse`. This will reverse the order of the Latest news cards.

### 3. Simplify services list

**[Mandatory]**

Using the files from the previous task, remove the second `ul` in the Services section of `3-index.html`, and put the three `li` elements under the first `ul`.

In your CSS file, before `/*** 4. CARD ***/`, add a new comment: `/* Section SERVICES ============================= */`. Under that comment section, add a new selector targeting the `row` class inside the `section-services` class, and set the `flex-wrap` property to `wrap`.

### 4. Playing around with the spacing between flex service items

**[Mandatory]**

Using the files from the previous task, in the `4-styles.css` file, within the `Grid` section:

- In the `.col-1-3` selector, replace the current `width` with `calc((100% / 3) - 2rem)`.
- In the `.col-1-2` selector, replace the current `width` with `calc((100% / 2) - 2rem)`.
- In the `[class*='col-']` selector, remove the `padding` declaration and set the `margin` property to `1rem`.
- In the `ul.row` declaration, replace the current `margin` with `-1rem`.

### 5. Flexify the header

**[Mandatory]**

Using the files from the previous task, in your `5-index.html` file, inside the `Header` section:

1. Wrap the `div` with class `header-logo` and the `nav` with class `navbar-menu` with a `div` that has the class `header-container`.

In your `5-styles.css` file:

2. Inside the `/* Header` section, add a selector for the `header-container` class.
3. Set the `display` property to `flex` and the `justify-content` property to `space-between`.
4. Remove the `header-logo` and `header-logo a` rules.
5. Remove the `navbar-menu` rule.
6. In the `variables` section, remove the following variables:
   - `header-logo-position`
   - `header-logo-link-display`
   - `header-logo-link-position`
   - `header-logo-link-top`
   - `header-logo-link-left`

### 6. Flexify the navbar

**[Mandatory]**

Using the files from the previous task, in `6-styles.css`, inside the `/* Navbar` section:

1. In the `nav` class selector, set the `display` property to `flex`.
2. Inside the `.nav .nav-item` selector, remove the `display` declaration.
3. Target `.nav-item + .nav-item` inside the `nav` class and move the `margin` declaration from `.nav .nav-item` inside the new selector.
4. In the `variables` section, change the value of the `nav-item-margin` variable to `0 0 0 2rem`.

### 7. Align center logo and navbar

**[Mandatory]**

Using the files from the previous task, in `7-styles.css`, inside the `/* Header` section, in the `header-container` class selector, set the `align-items` property to `center`.

### 8. Simplify the hero banner

**[Mandatory]**

Using the files from the previous task, in `8-styles.css`, inside the `/* Section HERO` section:

1. In the selector targeting the `section-inner` class inside the `section-hero` class, remove the `padding` and replace it with the following properties:
   - `display: flex`
   - `flex-direction: column`
   - `align-items: flex-start`
   - `justify-content: center`
   - `min-height: 50vh`

### 9. Better alignment about us

**[Mandatory]**

Using the files from the previous task, in `9-styles.css`, after the `/* Section SERVICES` section, create a `/* Section ABOUT US` section. Inside that new section, target all classes that begin with `col-` inside the `section-about-us` class and set the `align-self` property to `center`.

### 10. Create an article and update hero styles

**[Advanced]**

Using the CSS file from the previous task and 10-article.html:

In 10-styles.css, inside the /* Section HERO */ section:
Add a new class selector .hero-homepage after .section-hero
Move all declarations from .section-hero inside .hero-homepage
Set position: relative and margin-top: -8.5rem for .section-hero
Set padding: 10rem 4rem for .section-body inside .section-hero
Set color: var(--color-white) and text-transform: uppercase for .section-category inside .section-hero

### 11. Update the new hero banner

**[Advanced]**

In 11-article.html:

Add class hero-article to the <header> inside <main>
Set background-image inline style for the <header>
Inside the section with class section-inner, add <span> with class section-category and text "Digital Life"
Add <h1> with class section-title and text "Ut alios omittam, hunc appello, quem ille unum secutus est"
In 11-styles.css, after the existing styles:
Target .hero-article class:
Set background-size: 150rem 100rem and background-position: 50% 0
Target the pseudo-element ::before of .hero-article:
Set content: empty, background: rgba(0, 0, 0, 0.8), and position properties

### 12. Structure the main article

**[Advanced]**

In 12-article.html:

After the <header> in the Hero section, create a <div> with class main-article
Inside main-article, create a <div> with class container and a <div> with class post
Inside post, create an <article> with class post-content
Add the comment <!-- Aside section --> after post-content and create an <aside> with class post-aside
Inside post-aside, create two <div>s with classes post-meta and post-share
In 12-styles.css, after the existing styles:
Target .main-article class and set padding: 5rem 0
Add styles for post structure with comments

### 13. Meta list inside the aside section

**[Advanced]**

In 13-article.html:

Create an unordered list with classes post-meta-list and row inside post-meta div
Create <li>s for author, date, and tags with respective classes
Style the list and tags in 13-styles.css as per the instructions provided

### 14. Add the share social icons

**[Advanced]**

In 14-article.html:

Inside post-share div, copy the social nav list from the footer and remove Instagram
Replace the hrefs with default values (#)
Update 14-styles.css with necessary styles for social share icons

### 15. Finalizing the article

**[Advanced]**

In 100-article.html:

Add paragraphs, headings, images, blockquotes, and links as instructed
Wrap specific text with <b> tags and create <figure> with <img> and <figcaption>
Add <blockquote>, <a> with target _blank, and <ul> with <li>s
Update 100-styles.css with styling for images and content as instructed

### 16. Timemachine boxes!

**[Advanced]**

Create a CSS file 101-style.css that displays a set of boxes in a specific layout using flexbox.

Choose custom colors for each box and use flex layout to position them
Avoid using float, text-align, margin, or padding
Utilize provided HTML file 101-index.html

