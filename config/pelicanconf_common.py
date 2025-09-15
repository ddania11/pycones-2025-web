# -*- coding: utf-8 -*-
from datetime import datetime
from collections import OrderedDict
import pytz


from pelicanconf_flags import *
from pelicanconf_event import CALL_FOR_PAPERS_LINK

AUTHOR = "Python España Org"
SITENAME = "PyConES 2025 Sevilla"
PATH = "content"
THEME = "theme"
PLUGIN_PATHS = ["plugins"]

TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "es"
DEFAULT_DATE_FORMAT = "%d/%M/%Y"
MARKUP = ("md",)
PLUGINS = ["i18n_subsites", "assets"]
STATIC_PATHS = ["images", "extra/manifest.json"]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n", "extensions.gphotos.GPhotosExtension"],
}


DIRECT_TEMPLATES = [
    "index",
    "blog",
    "keynoters",
    "sponsorship",
    "schedule",
    "gallery",
    "past_editions",
    "organizers",
    "tickets",
    "jobs",
]


MENUITEMS_NAVBAR = OrderedDict(
    {
        "Dónde": OrderedDict(
            {
                "Sevilla, el marco": "/pages/sevilla.html",
                "Universidad Pablo de Olavide, la sede": "/pages/upo.html",
                "Cómo llegar": "/pages/how-to-arrive.html",
                "Dónde alojarse": "/pages/where-staying.html",
            }
        ),
        "Organización": OrderedDict({"Equipo": "/organizers.html"}),
        "Diversidad": OrderedDict(
            {
                "Código de Conducta": "/pages/code-of-conduct.html",
                "Becas": "/becas.html",
            }
        ),
    }
)

if CALL_FOR_PAPERS_LINK and ENABLED_CALL_FOR_PAPERS:
    MENUITEMS_NAVBAR["Llamada a ponentes"] = OrderedDict(
        {
            "url": CALL_FOR_PAPERS_LINK,
            "target": "_blank",
            "external": True,
        }
    )

if ENABLED_TICKETS:
    MENUITEMS_NAVBAR["Tickets"] = "/tickets.html"

if ENABLED_SPEAKERS:
    MENUITEMS_NAVBAR["Ponentes"] = "/keynoters.html"

if ENABLED_SPONSORSHIPS:
    MENUITEMS_NAVBAR["Patrocinios"] = "/sponsorship.html"

if ENABLED_TIMETABLE:
    MENUITEMS_NAVBAR["Horario"] = "/schedule.html"

if ENABLED_GALLERY:
    MENUITEMS_NAVBAR["La ciudad"]["Galería"] = "/gallery.html"

if ENABLED_PAST_EDITIONS:
    MENUITEMS_NAVBAR["Organización"]["Ediciones pasadas"] = "/past_editions.html"

if ENABLED_JOBS:
    MENUITEMS_NAVBAR["Ofertas de trabajo"] = "/jobs.html"

if ENABLED_DJANGO_GIRLS:
    MENUITEMS_NAVBAR["Django Girls"] = "/pages/django-girls.html"

if ENABLED_BLOG:
    MENUITEMS_NAVBAR["Blog"] = "/blog.html"

MENUITEMS_NAVBAR.move_to_end("Tickets", last=False)

NAVBAR_STYLE = "is-primary"
THEME_LOGO = "/theme/images/logos/ICONO_ORIGINAL.png"  # navbar
MAIN_LOGO = "/theme/images/logos/PYCONES_CORTADO.png"  # logo principal
MAIN_LOGO_PNG = "/theme/images/logos/PYCONES_ORIGINAL_AZUL.png"  # logo que se muestra en redes sociales


FOOTER = "Copyright © Python España & PyConES 2025 Org"
THEME_COLOR = "#0E749CFF"
LAST_UPDATE = datetime.now(pytz.timezone(TIMEZONE)).strftime("%B %d, %Y %A, %H:%M:%S")
