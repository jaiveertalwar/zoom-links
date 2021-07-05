import rumps
import webbrowser

@rumps.clicked("Math")
def about(sender):
    webbrowser.open('link here')

@rumps.clicked("English")
def about(sender):
    webbrowser.open('link here')

@rumps.clicked("Science")
def about(sender):
    webbrowser.open('link here')

@rumps.clicked("Arabic")
def about(sender):
    webbrowser.open('link here')

@rumps.clicked("Spanish")
def about(sender):
    webbrowser.open('link here')

@rumps.clicked("Art")
def about(sender):
    webbrowser.open('link here')

@rumps.clicked("Singing")
def about(sender):
    webbrowser.open('link here')

@rumps.clicked("ℹ")
def about(sender):
    rumps.alert('Classes v1.0 by JTLR Development, credit JTLR ')

app = rumps.App("Classes", title='🔐')
app.menu = [
    rumps.MenuItem('JTLR Development', icon='icon.png', dimensions=(18, 18)),
    'v1.0.1 by jtlr.cf',
]
app.run()
