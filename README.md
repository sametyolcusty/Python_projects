def create_readme(website, social_media):
    readme_content = f"""# My Awesome Project

Welcome to my awesome project!

## About

This project aims to ...

## Usage

To use this project, ...

## Website

Visit my website: [{website}](https://www.sametyolcu.com/portfolio)

## Social Media

Follow me on:
- Twitter: [{social_media['twitter']}]({social_media['twitter']})
- LinkedIn: [{social_media['linkedin']}]({social_media['linkedin']})
- Stack Overflow: [{social_media['stackoverflow']}]({social_media['stackoverflow']})
"""

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

# Replace the placeholders with your website and social media links
my_website = "https://www.sametyolcu.com/portfolio"
my_social_media = {
    'twitter': 'https://twitter.com/sametylcu',
    'linkedin': 'https://www.linkedin.com/in/samet-yolcu',
    'stackoverflow': 'https://stackoverflow.com/users/23614045/samet-yolcu'
}

# Create the README file
create_readme(my_website, my_social_media)




