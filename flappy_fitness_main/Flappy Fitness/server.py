# server.py
import socketio

# Create a Socket.IO server
sio = socketio.Server()

# Event to handle client connection
@sio.event
def connect(sid, environ):
    print('Client connected:', sid)

# Event to handle client disconnection
@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)

# Event to handle jumping jack detection
@sio.event
def jumping_jack(sid, data):
    print('Jumping jack detected:', data)
    sio.emit('flappy_bird_move', {'action': 'move_up'})

# Wrap with the built-in eventlet WSGI server
if __name__ == '__main__':
    import eventlet
    import eventlet.wsgi
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)