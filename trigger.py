#!/usr/bin/env python3

from collections import OrderedDict

import sublime, sublime_plugin


XSMALL = "xsmall"
SMALL = "small"
MEDIUM = "medium"
LARGE = "large"
XLARGE = "xlarge"
DEFAULT_SIZE = XSMALL


VALUES = OrderedDict()
VALUES[XSMALL] = {
    "font_size": 12,
    "theme_font_xs": True,
    "theme_sidebar_indent_xs": True,
    "theme_sidebar_size_xs": True,
    "theme_size_xs": True,
}
VALUES[SMALL] = {
    "font_size": 14,
    "theme_font_sm": True,
    "theme_sidebar_indent_sm": True,
    "theme_sidebar_size_sm": True,
    "theme_size_sm": True,
}
VALUES[MEDIUM] = {
    "font_size": 16,
    "theme_font_md": True,
    "theme_sidebar_indent_md": True,
    "theme_sidebar_size_md": True,
    "theme_size_md": True,
}
VALUES[LARGE] = {
    "font_size": 18,
    "theme_font_lg": True,
    "theme_sidebar_indent_lg": True,
    "theme_sidebar_size_lg": True,
    "theme_size_lg": True,
}
VALUES[XLARGE] = {
    "font_size": 20,
    "theme_font_xl": True,
    "theme_sidebar_indent_xl": True,
    "theme_sidebar_size_xl": True,
    "theme_size_xl": True,
}


SIZES = list(VALUES.keys())


class PreferencesToggleCommand(sublime_plugin.TextCommand):

    def run(self, edit, *args, increment=None, is_size=None, **kwargs):
        settings = sublime.load_settings('Preferences.sublime-settings')

        if increment == "-":
            increment = -1
        else:
            increment = 1

        if is_size not in SIZES:
            try:
                next_size = (SIZES.index(settings.get('size')) + increment) % len(SIZES)
                next_size = SIZES[next_size]
            except:
                next_size = DEFAULT_SIZE
        else:
            next_size = is_size

        # clear all current values
        for _, preferences in VALUES.items():
            for k, _ in preferences.items():
                settings.erase(k)

        # set the new values
        sublime.status_message("[SP] Size={}".format(next_size))
        settings.set("size", next_size)
        for k, v in VALUES[next_size].items():
            settings.set(k, v)

        sublime.save_settings('Preferences.sublime-settings')
