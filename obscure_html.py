import sublime, sublime_plugin

from random import randint

class ObscureHtmlCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    sels = self.view.sel()
    for sel in sels:
      text = self.view.substr(sel)
      fuzz = []
      for c in text:
        if randint(0, 9) < 5:
          # ascii encode
          fuzz.append('&#%s;' % str(ord(c)))
        else:
          # hex encode
          fuzz.append('&#%s;' % hex(ord(c)).lstrip('0'))
      self.view.replace(edit, sel, ''.join(fuzz))
    return

