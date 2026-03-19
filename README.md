# calcms
Python and React-based CMS

# Roadmap
## P0
- Configuration (Make files, etc)
- Python webserver for the API, likely on FastAPI (Done, inital)
- Main DB setup. Layered so that users can select which to use (eg, not opinionated). Personal setup will likely use Postgre. (Initial, done)
- Frontend on vite/react/etc, using Panda CSS and radix
- Ability to get posts/pages from DB and send them to front end to display
- Configurable site rather than hardcoded

## P1
- Begin creation of CMS backend
- Start adding in rich text editor for CRUD applications on pages/posts
- Uploading of assets (eg images)

## P2
- Templates and theming
- Plugins support?
- Basic configuration flow

## P3
- Backup and restoration of DB
- Updating from CDN
- WYSWIG for templates