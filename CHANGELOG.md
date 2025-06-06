# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure with directories for `srcs`, `certbot`, `frontend`, `frontend-rust`, and `nginx`.
- Configurations for `docker-compose.yml` and `Dockerfile` in `frontend-rust` for building and running the frontend application.
- Certbot configurations in `srcs/certbot/conf` for managing SSL certificates.
- Frontend assets in `srcs/frontend` including `images/image.webp` and `index.html`.
- Rust-based frontend in `frontend-rust/curriculum` with Yew setup and dependencies.
- Nginx configurations (`default.conf` and `nginx.conf`) for hosting and serving the application.
- `Makefile` for managing project build tasks.
- Fully functional Dockerized project environment, combining Nginx, Rust frontend, and Certbot for HTTPS setup.
- Support for SSL certificate generation and renewal using Certbot.
- Integrated build process for Rust-based frontend application using Yew.
- Docker Compose configuration for multi-container orchestration.
- Initial deployment scripts and example files for hosting the CV site on a production server.
