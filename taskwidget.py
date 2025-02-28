# -*- coding: latin-1 -*-
import urwid

class TaskWidget (urwid.WidgetWrap):

    def __init__ (self, task):
        self.task = task

        desc = task.description()
        if  self.task.status() == 'completed':
            desc = '✓ ' + desc.encode('cp1250')
        else:
            desc = '  ' + desc
        desc = urwid.Text(desc)

        proj = urwid.Text(task.project() + ' ', align='right')

        due  = urwid.Text(task.due_date_string() + ' ', align='right')
        tags = urwid.Text(task.tags_string() + ' ', align='right')

        (style, style_focus) = ('body', 'body_focus')
        if (task.start_date() is not None):
            (style, style_focus) = ('body_emph', 'body_emph_focus')

        item = urwid.AttrMap(urwid.Columns([
            ('fixed', 11, urwid.AttrWrap(proj, 'proj', 'proj_focus')),
            desc,
            tags,
            ('fixed', 11, due)
        ]), style, style_focus)

        urwid.WidgetWrap.__init__(self, item)

    def selectable (self):
        return True

    def keypress(self, size, key):
        return key

