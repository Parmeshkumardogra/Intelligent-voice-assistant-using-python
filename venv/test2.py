import pyglet

ag_file = "1.gif"

animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

win = pyglet.window.Window(width=sprite.width, height=sprite.height)

@win.event
def on_draw():
    win.clear()
    sprite.draw()

def close(event):
    win.close()

pyglet.clock.schedule_once(close, 1.0)

pyglet.app.run()