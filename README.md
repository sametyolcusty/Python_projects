
# Welcome to my python projects

I am trying to produce various projects such as data analysis projects and subject comprehension projects using the Python language. 

You can also find all my projects in my website.

## Website

Visit my website: {website}

## Social Media

Follow me on:
- Twitter: {social_media['twitter']}
- LinkedIn: {social_media['linkedin']}
- StackOverflow: {social_media['stackoverflow']}
"""

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)


my_website = "https://www.sametyolcu.com/portfolio"
my_social_media = {
    'twitter': 'https://twitter.com/sametylcu',
    'linkedin': 'https://www.linkedin.com/in/samet-yolcu',
    'stackoverflow': 'https://stackoverflow.com/users/23614045/samet-yolcu'
}

create_readme(my_website, my_social_media)


